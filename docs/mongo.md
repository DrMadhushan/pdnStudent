Now to install mongodb use

    brew tap mongodb/brew

    brew install mongodb-community@6.0

To check if mongodb has been installed use

    mongosh --version

to start mongoDB as macOS service use

    brew services start mongodb-community@6.0

and to stop mongoDB to run as a background service use

    brew services stop mongodb-community@6.0

Or, if you don't want/need a background service you can just run:

    mongod --config /opt/homebrew/etc/mongod.conf

To run mongodb commands, open a new table and run 

    mongosh

To check your databases run 
    
    show dbs

