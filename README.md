## Log Parsing Exercise

This project contains an attempt at solving [LogMessageParsingProblem](./ProblemStatement.pdf)

#### Basic overview of problem

Each log message will have 3 parts: 
`[message type] [timestamp] [message]`

A message type can be: `Information` `Warning` `Error <Log Level>`

#### Expected Behaviour

The application when parses a log message should get transformed to a format denoting the properties of the log message 
like shown below.

| LogMessage        | Parsed Log Message           |
| ------------- |:-------------:|
| I 6 Completed processing | Information 6 "Completed processing"|
| W 6 Completed processing | Warning 6 "Completed processing"|
| E 2 6 Completed processing | (Error 2) 6 "Completed processing"|
