// This is a read operation on 'local' database

DB = db.getSiblingDB('local');
DB.startup_log.find();
