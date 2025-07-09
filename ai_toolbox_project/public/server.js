//---------------------------------------Server Setup Sektion------------------------------------//

const express = require('express');
const cors = require('cors');

// import the predefined dbSchema
const Tool = require('./models/dbTools.js');

// import dotenv to create local variables
const dotenv = require('dotenv');

// to receive data out of the .env file
dotenv.config();

// nodemailer -> automatic emailGenerator
const nodemailer = require('nodemailer');

// use mongoose for better control of the database
const mongoose = require('mongoose');

const app = express();

// import logger -> log server responses and potential errors
const logger = require('./logger.js');

// database conection aus der .env file holen -> security
mongoose.connect(process.env.MONGO_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => logger.info('Mongoose verbunden mit MongoDB'))
.catch(err => logger.error('Mongoose-Verbindung fehlgeschlagen:', err));

const port = process.env.PORT;

// CORS-Middleware for all domains
app.use(cors());
// JSON parsing middleware
app.use(express.json());

// Server Test
app.get('/', (req, res) => {
  res.send('Server ist live!');
});

// rounding function for the star rating
function roundToStars(wert){
  const starRounded = Math.round(wert*2) /2;
  return starRounded;
}

//----------------------------------------------Database Section---------------------------------------------//

// get all tools from the databse
app.get('/get-data' , async (req , res) => {

    try{
        // find() -> return all document out of the collection -> as an array of objects
        const data = await Tool.find();
        // send data to client 
        res.json(data);
        logger.info('Get-Anfrage auf Datenbank erfolgreich.');
    } catch (error){
        logger.error(`Fehler im Get Handler : ${err.message} `);
        res.status(500).json({
            message : 'Ein Fehler bei der Datenübertragung ist aufgetreten.'
        });
    }
});

// server gets data from the client -> adds a new entry to the database
app.post('/add-entry', async (req, res) => {
    const {uploaderName , uploaderEmail, uploadType , uploadDate , ageRecommendation , uploadTitle,
            uploadDescription , fileURL , thumbnailURL , uploadTags } = req.body;

    try {

        const newEntry = new Tool({
            uploaderName: uploaderName ,
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

        // save the new entry in the database
        await newEntry.save();

        logger.info('Datenbankeintrag erfolgreich eingefügt.')
        res.status(200).send('Daten erfolgreich gespeichert!');
    } catch (error) {
        logger.error(`Fehler beim Speichern der Daten` , error);
        res.status(500).send('Interner Serverfehler.');
    }
});

//----------------------------------------------E-Mail Transporter Section---------------------------------------------//

// .env-check -> are all infos there we need to send an email
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

//------------------------------------------------Email Section new Submission-----------------------------------------//

app.post('/send-email-submit', (req, res) => {
  const { to } = req.body;

  // email structure -> to user
  const mailOptionsUser = {
    from: process.env.EMAIL_USER,
    to: to,
    subject: 'Thank you for your submission!',
    text: 'Thank you for submitting your project! We appreciate your contribution. Our team will review it soon.\n\nBest regards,\nThe Team'
  };

  // email structure -> to ourselfs
  const mailOptionsSelf = {
    from: process.env.EMAIL_USER,
    to: process.env.EMAIL_USER,
    subject: 'New Toolbox!',
    text: 'A new Toolbox is available for review step!'
  };

    // first email to email-adress that submitted -> succes feedback
    transporter.sendMail(mailOptionsUser, (errUser, infoUser) => {
      if (errUser) {
        logger.error(`Fehler beim Senden an User: ${errUser.message}`);
        return res.status(500).send('E-Mail an Nutzer konnte nicht gesendet werden: ' + errUser.message);
      }
      logger.info('E-Mail erfolgreich an User gesendet: ' + infoUser.response);

    // second email to ourselfs to be informed there is a new submission -> information
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
//--------------------------------------------Email Section Contact----------------------------------------//

app.post('/send-email-contact', async (req, res) => {
  try {
    const { name, emailFrom, message } = req.body;

    // server response with an error if something is missing
    if (!name || !emailFrom || !message) {
      return res.status(400).send('Bitte alle Felder ausfüllen.');
    }

    // mail infos to colaps -> structure     
    const mailOptionsColaps = {
      from: process.env.EMAIL_USER,
      to: 'colapsresearch@gmail.com',
      subject: 'Contact Page',
      text: `
        Contact by: ${name}
        Contact from Email: ${emailFrom}
        Contact message:
        ${message}
      `.trim()
    };

    const info = await transporter.sendMail(mailOptionsColaps);
    logger.info(`E-Mail erfolgreich gesendet: ${info.response}`);
    res.status(200).send('E-Mail erfolgreich an colaps gesendet.');

  } catch (err) {
    logger.error(`Fehler beim E-Mail-Versand: ${err.message}`);
    res.status(500).send('Fehler beim E-Mail-Versand: ' + err.message);
  }
});

//--------------------------------------------Server Start Section----------------------------------------//

app.listen(port, () => {
  logger.info(`Server läuft auf http://localhost:${port}`);
});

//--------------------------------------------Rating Toolbox Section----------------------------------------//

app.patch('/rate-toolbox', async (req, res) => {
  const { toolboxId, rating } = req.body;

  // Json returns String -> parse to number!
  const ratingNumber = Number(rating);

  try {
    const toolbox = await Tool.findById(toolboxId);
    if (!toolbox){
      return res.status(404).send('Toolbox nicht gefunden');
    } 

    // add the new rating to the array
    toolbox.rating.totalRatings.push(ratingNumber); 

    // get number of total ratings -> to compute avarage
    toolbox.rating.ratingCount = toolbox.rating.totalRatings.length;

    // compute the sum of all ratings in the array
    const sum = toolbox.rating.totalRatings.reduce((acc, cur) => acc + cur, 0);

    // compute avarage star rating -> not rounded
    const wildAvarage = sum / toolbox.rating.ratingCount;

    // round to fit into the star rating
    const starRounded = roundToStars(wildAvarage);

    // update avarage rating
    toolbox.rating.averageRating = starRounded;

    await toolbox.save();
    logger.info('Bewertung erfolgreich abgegeben.');

    res.send({ success: true, toolbox });
  } catch (err) {
    res.status(500).send('Fehler beim Speichern der Bewertung');
    logger.error(`Fehler beim Speichern der Bewertung : ${err.message}`);
  }
});

