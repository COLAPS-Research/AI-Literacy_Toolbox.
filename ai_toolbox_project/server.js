// =================================================================
//                 AI LITERACY TOOLBOX - FINAL SERVER
// =================================================================
// This server integrates all functionalities into a robust and
// maintainable architecture.
// =================================================================

// --- 1. IMPORTS & INITIAL SETUP ---
const express = require('express');
const path = require('path');
const cors = require('cors');
const mongoose = require('mongoose');
const nodemailer = require('nodemailer');
const logger = require('./logger');
const Tool = require('./models/dbTools');
require('dotenv').config();

const app = express();

// --- 2. CONFIGURATION & CONSTANTS ---
const PORT = process.env.PORT || 8080;
const MONGO_URI = process.env.MONGO_URI;
const basePath = process.env.BASE_PATH || '/ai-literacy-toolbox';

// Email Transporter Configuration
const mailerTransporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: process.env.SMTP_PORT,
    secure: false, // false for port 587
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS,
    },
});

// --- 3. HELPER FUNCTIONS ---
function roundToStars(wert) {
    const starRounded = Math.round(wert * 2) / 2;
    return starRounded;
}

// --- 4. CORE MIDDLEWARE ---
app.use(cors());
app.use(express.json());
app.use((req, res, next) => {
    logger.info(`Incoming Request: ${req.method} ${req.originalUrl}`);
    next();
});

// --- 5. API ROUTER DEFINITION ---
const apiRouter = express.Router();

// Health Check Route
apiRouter.get('/status', (req, res) => res.status(200).json({ status: 'API is healthy' }));

// Get All Tools Route
apiRouter.get('/get-data', async (req, res) => {
    try {
        const data = await Tool.find();
        logger.info('Successfully fetched all tool data.');
        res.status(200).json(data);
    } catch (error) {
        logger.error(`Error in /get-data handler: ${error.message}`);
        res.status(500).json({ message: 'Error fetching data from database.' });
    }
});

// Add a New Tool Route
apiRouter.post('/add-entry', async (req, res) => {
    try {
        const newTool = new Tool(req.body);
        await newTool.save();
        logger.info(`Successfully saved new tool: ${newTool.uploadTitle}`);
        res.status(201).json({ message: 'Tool submitted successfully!', tool: newTool });
    } catch (error) {
        logger.error(`Error saving new tool entry: ${error.message}`);
        res.status(500).json({ message: 'Error saving tool to the database.' });
    }
});

// Send Submission Confirmation Email Route
apiRouter.post('/send-email-submit', async (req, res) => {
    const { to } = req.body;
    if (!to) return res.status(400).json({ message: 'Recipient email ("to") is required.' });

    try {
        // Send email to the user
        await mailerTransporter.sendMail({
            from: `"AI Literacy Toolbox" <${process.env.EMAIL_USER}>`,
            to: to,
            subject: 'Thank you for your submission!',
            text: 'We have received your tool submission and will review it shortly. Thank you for contributing!',
        });
        logger.info(`Submission confirmation email sent to: ${to}`);

        // Send notification email to the admin
        await mailerTransporter.sendMail({
            from: `"AI Toolbox System" <${process.env.EMAIL_USER}>`,
            to: process.env.EMAIL_USER, // Sends to yourself
            subject: 'New Toolbox Submission for Review!',
            text: `A new tool has been submitted by ${to}. Please review it in the admin panel.`,
        });
        logger.info('Admin notification email sent.');

        res.status(200).json({ message: 'Confirmation emails sent successfully.' });
    } catch (error) {
        logger.error(`Error sending submission emails: ${error.message}`);
        res.status(500).json({ message: 'Failed to send submission emails.' });
    }
});

// Send Contact Form Email Route
apiRouter.post('/send-email-contact', async (req, res) => {
    const { name, emailFrom, message } = req.body;
    if (!name || !emailFrom || !message) {
        return res.status(400).json({ message: 'Name, email, and message are required.' });
    }

    try {
        await mailerTransporter.sendMail({
            from: `"Contact Form" <${process.env.EMAIL_USER}>`,
            to: process.env.EMAIL_COLAPS, // IMPORTANT: Ensure this is in your .env file
            subject: `New Contact Message from ${name}`,
            text: `From: ${name} <${emailFrom}>\n\nMessage:\n${message}`,
        });
        logger.info(`Contact form email sent successfully from: ${emailFrom}`);
        res.status(200).json({ message: 'Contact message sent successfully.' });
    } catch (error) {
        logger.error(`Error sending contact form email: ${error.message}`);
        res.status(500).json({ message: 'Failed to send contact message.' });
    }
});

// Rate a Toolbox Route
apiRouter.patch('/rate-toolbox', async (req, res) => {
    const { toolboxId, rating } = req.body;
    if (!toolboxId || rating === undefined) {
        return res.status(400).json({ message: 'Tool ID and rating are required.' });
    }

    try {
        const toolbox = await Tool.findById(toolboxId);
        if (!toolbox) return res.status(404).json({ message: 'Toolbox not found.' });

        toolbox.rating.totalRatings.push(Number(rating));
        toolbox.rating.ratingCount = toolbox.rating.totalRatings.length;
        const sum = toolbox.rating.totalRatings.reduce((acc, cur) => acc + cur, 0);
        toolbox.rating.averageRating = roundToStars(sum / toolbox.rating.ratingCount);

        await toolbox.save();
        logger.info(`Successfully updated rating for toolbox ID: ${toolboxId}`);
        res.status(200).json({ success: true, toolbox });
    } catch (error) {
        logger.error(`Error saving rating: ${error.message}`);
        res.status(500).json({ message: 'Error saving rating.' });
    }
});

// Mount the entire API router to the correct base path
app.use(`${basePath}/api`, apiRouter);


// --- 6. STATIC FILE SERVER & FRONTEND ROUTING ---
app.use(basePath, express.static(path.join(__dirname, 'public')));
app.get(`${basePath}/*`, (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


// --- 7. DATABASE CONNECTION & SERVER START ---
logger.info('Application starting...');
mongoose.connect(MONGO_URI)
    .then(() => {
        logger.info('MongoDB connection established successfully!');
        app.listen(PORT, () => {
            logger.info(`Server is now listening on port ${PORT}`);
            logger.info(`Access the application at: http://localhost${basePath}`);
        });
    })
    .catch(err => {
        logger.error('FATAL ERROR: Could not connect to MongoDB.', err);
        process.exit(1);
    });
