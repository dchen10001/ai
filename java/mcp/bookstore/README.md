# MCP Book Store Server

1. Goto https://start.spring.io/
	select java, maven, jdk 21, spring boot 4.0.5

2. Unzip the file, and import the project to Eclipse

3. use prompts.md to generate code, and test cases, and make sure the test coverage is 100% for all the methods.

4. run the application, and make sure it works without any error.

5. move bookstore-0.0.1-SNAPSHOT-exec.jar under target to repo folder, and run the command: java -jar bookstore-0.0.1-SNAPSHOT-exec.jar, make sure it works without any error.

6. configure MCP server in Eclipse (it can be configured in VS, Claude Desktop App as well)
   click edit preferences icon of Copilot Chat (the gear icon on the top right corner of the chat window),
   select Model Context Protocol(MCP Server), copy below json string, and save.
   
   
{
  "servers": {
   "java_book_server": {
      "command": "java",
      "args": [
        "-jar",
        "C:/development/claude/repo/bookstore-0.0.1-SNAPSHOT-exec.jar"
      ]
    }
  }
}