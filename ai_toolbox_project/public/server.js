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





// --- Define the Application's Base Path ---
const basePath = process.env.BASE_PATH || '/';
// --- API Router Setup ---
const apiRouter = express.Router();

// Define all your API routes here
// This will be accessible at GET /ai-literacy-toolbox/api/status
apiRouter.get('/status', (req, res) => res.json({ status: 'API is healthy' }));

// This will be accessible at POST /ai-literacy-toolbox/api/add-entry
apiRouter.post('/add-entry', async (req, res) => {
    // Your logic to save a new tool
    res.send('Tool submitted!');
});

// Mount the API router AT THE CORRECT PATH
app.use(`${basePath}/api`, apiRouter);

// --- Static File Server ---
// Serve the 'public' folder from the base path. This makes your website visible.
// A request for /ai-literacy-toolbox/style.css will serve the file public/style.css
app.use(basePath, express.static(path.join(__dirname, 'public')));

// --- Catch-all for Frontend Routing ---
// This ensures that if a user refreshes on /ai-literacy-toolbox/about.html,
// your app still serves the main HTML page.
app.get(`${basePath}/*`, (req, res) => {
    res.sendFile(path.join(__dirname, 'public', '/index.html'));
});


// ... your database connection and app.listen logic ...
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));










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

// configure email transporter -> from where do we send 
// read sensible data out of .env to secure the data
// process.env.blablabla -> global object which reads the value out of .env 
const transporter = nodemailer.createTransport({

  // define mailservice and 'login' from sender-email
  host: process.env.SMTP_HOST,       //  SMTP-Server 
  port: process.env.SMTP_PORT,       //  Portnummer: 587 für STARTTLS, 465 für SSL/TLS, 25 ist oft blockiert
  secure: false,                     //  true = SSL/TLS (Port 465), false = STARTTLS (587)

  requireTLS: true,                  //  force TLS-Encryption -> most of the time a must have

  auth: {
    user: process.env.EMAIL_USER,     //  from what email do we send 
    pass: process.env.EMAIL_PASS      //  App-specific password -> not the normal passwort (but would also work)
  }
});
/*
  // optional fields -> for when the projects grows bigger

  name: 'mein-client.local',         //  (optional) own hostname and handshake -> not in production
  tls: {
    rejectUnauthorized: false        //  for testing , own signed significate –> not in production
  },
  pool: true,                       //  (Optional) activates connectionPool for more Emails
  maxConnections: 5,                //  (Optional) Max. simult. connections (only if -> pool: true)
  maxMessages: 100,                 //  (Optional) Max. number of emails per connection
  rateDelta: 1000,                  //  (Optional) Minimum time in ms between 2 emails
  rateLimit: 5,                     //  (Optional) Max. emails per second -> good to reduce 
  logger: true,                     //  activates logger fpr transport purposes -> debug 
  debug: true                       //  shows debug messages in the console
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
      to: EMAIL_COLAPS ,
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

