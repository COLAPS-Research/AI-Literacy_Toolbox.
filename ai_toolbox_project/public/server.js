//---------------------------------------Server Setup Sektion------------------------------------//

const express = require('express');
const cors = require('cors');

// import the predefined dbSchema
const Tool = require('./models/dbTools.js');
const dotenv = require('dotenv');

// um Daten aus der .env-Datei zu erhalten
dotenv.config();

// nodemailer -> automatic emailGenerator
const nodemailer = require('nodemailer');

// Nur Mongoose verwenden
const mongoose = require('mongoose');

const app = express();

// logger importieren
const logger = require('./logger.js');

// database conection aus der .env file holen -> security
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => logger.info('Mongoose verbunden mit MongoDB'))
.catch(err => logger.error('Mongoose-Verbindung fehlgeschlagen:', err));

const port = process.env.PORT;

// CORS-Middleware für alle Domains (Entwicklung)
app.use(cors());
// JSON parsing middleware
app.use(express.json());

// Server Test
app.get('/', (req, res) => {
  res.send('Server ist live!');
});

//----------------------------------------------Database Section---------------------------------------------//

// der Server sendet Daten an den Clienten mit der GET Anfrage
app.get('/get-data' , async (req , res) => {

    try{
        // mit find() werden alle Dokumente aus der Collection abgerufen -> gibt Array aus Objekten(Dokumenten) zurück
        const data = await Tool.find();
        // sendet Daten an den Clienten und beendet die Anfrage
        res.json(data);
        logger.info('Get-Anfrage auf Datenbank erfolgreich.');
    } catch (error){
        logger.error(`Fehler im Get Handler : ${err.message} `);
        res.status(500).json({
            message : 'Ein Fehler bei der Datenübertragung ist aufgetreten.'
        });
    }
});

// der Server erhält Daten vom Clienten mit der POST Anfrage
app.post('/add-entry', async (req, res) => {
    const {uploaderEmail, uploadType , uploadDate , ageRecommendation , uploadTitle,
            uploadDescription , fileURL , thumbnailURL , uploadTags } = req.body;

    try {

        const newEntry = new Tool({
            uploaderEmail: uploaderEmail ,
            uploadType: uploadType ,
            uploadDate: uploadDate ,
            ageRecommendation: ageRecommendation ,
            uploadTitle: uploadTitle ,
            uploadDescription: uploadDescription ,
            fileURL: fileURL ,
            thumbnailURL: thumbnailURL ,
            uploadTags: uploadTags ,
        });

        // neuen Db Eintrag abspeichern
        await newEntry.save();

        logger.info('Datenbankeintrag erfolgreich eingefügt.')
        res.status(200).send('Daten erfolgreich gespeichert!');
    } catch (error) {
        logger.error(`Fehler beim Speichern der Daten` , error);
        res.status(500).send('Interner Serverfehler.');
    }
});

//----------------------------------------------E-Mail Section---------------------------------------------//

// .env-check -> sind alle benötgten Informationen auch vorhanden zum Email Versandt
if (!process.env.EMAIL_USER || !process.env.EMAIL_PASS) {
  logger.warn('Warnung: .env-Konfiguration scheint unvollständig zu sein!');
}

// Email-Transporter konfigurieren –> sagt aus über welchen Maildienst versendet wird
// env-Datei erstellen und in '.gitignore' schreiben um sensible Daten zu schützen
// process.env.blablabla -> gobales Objekt welches die privaten Werte aus der .env Datei ausliest
const transporter = nodemailer.createTransport({

  // === Pflichtfelder ===
  host: process.env.SMTP_HOST,       //  SMTP-Server (z. B. smtp.office365.com oder smtp.gmail.com)
  port: process.env.SMTP_PORT,       //  Portnummer: 587 für STARTTLS, 465 für SSL/TLS, 25 ist oft blockiert
  secure: false,                     //  true = SSL/TLS (Port 465), false = STARTTLS (587)

  requireTLS: true,                  //  TLS (Verschlüsselung) erzwingen –> sicherer und meist erforderlich

  auth: {
    user: process.env.EMAIL_USER,     //  Absenderadresse
    pass: process.env.EMAIL_PASS      //  App-spezifisches Passwort (nicht das normale email Passwort -> geht aber auch)
  }
});
/*
  // Optionale Felder -> vielleicht später wenn das projekt wächst

  name: 'mein-client.local',         //  (Optional) Eigener Hostname im SMTP-Handshake -> nicht in produktion
  tls: {
    rejectUnauthorized: false        //  Für Testserver mit selbstsignierten Zertifikaten –> nicht in produktion
  },
  pool: true,                       // (Optional) Aktiviert einen Verbindungspool für mehrere E-Mails
  maxConnections: 5,                //  (Optional) Max. gleichzeitige SMTP-Verbindungen (nur bei pool: true)
  maxMessages: 100,                 //  (Optional) Max. Anzahl E-Mails pro Verbindung
  rateDelta: 1000,                  //  (Optional) Minimalzeit (in ms) zwischen zwei Nachrichten
  rateLimit: 5,                     //  (Optional) Max. Nachrichten pro Sekunde (gut gegen Ratenbegrenzung)
  logger: true,                     //  Aktiviert Logging für Transport-Aktivitäten (Debug-Zwecke)
  debug: true                       //  Zeigt ausführliche Debug-Meldungen in der Konsole
*/

//------------------------------------------------Email Versand Sektion-----------------------------------------//

app.post('/send-email', (req, res) => {
  const { to } = req.body;

  // E-mail an den user -> aufbau
  const mailOptionsUser = {
    from: process.env.EMAIL_USER,
    to: to,
    subject: 'Thank you for your submission!',
    text: 'Thank you for submitting your project! We appreciate your contribution. Our team will review it soon.\n\nBest regards,\nThe Team'
  };

  // E-mail an uns selbst -> aufbau
  const mailOptionsSelf = {
    from: process.env.EMAIL_USER,
    to: process.env.EMAIL_USER,
    subject: 'New Toolbox!',
    text: 'A new Toolbox is available for review step!'
  };

    // erste E-Mail an User
    transporter.sendMail(mailOptionsUser, (errUser, infoUser) => {
      if (errUser) {
        logger.error(`Fehler beim Senden an User: ${errUser.message}`);
        return res.status(500).send('E-Mail an Nutzer konnte nicht gesendet werden: ' + errUser.message);
      }

      logger.info('E-Mail erfolgreich an User gesendet: ' + infoUser.response);

    // zweite E-Mail an uns selbst
    transporter.sendMail(mailOptionsSelf, (errSelf, infoSelf) => {
      if (errSelf) {
        logger.error(`Fehler beim Senden an uns selbst: ${errSelf.message}`);
        return res.status(500).send('E-Mail an User gesendet, aber E-Mail an Admin fehlgeschlagen: ' + errSelf.message);
      }

      logger.info('E-Mail erfolgreich an dich selbst gesendet: ' + infoSelf.response);
      res.status(200).send('Beide E-Mails wurden erfolgreich gesendet.');
    });
  });
});

app.listen(port, () => {
  logger.info(`Server läuft auf http://localhost:${port}`);
});

