const mongoose = require("mongoose");

const uri = "mongodb+srv://raybanpranavmahesh2023:<UixrwbHoHNs5EOjF>@lostperson.zgd2p.mongodb.net/"; 


mongoose.connect(uri, { 
    useNewUrlParser: true, 
    useUnifiedTopology: true 
}).then(() => {
    console.log("✅ Successfully connected to MongoDB!");
    process.exit(0);
}).catch(err => {
    console.error("❌ MongoDB connection failed:", err);
    process.exit(1);
});