<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>0x00. Personal data</h1>
        <hr>
        <h2> RESOURCES</h2>
        <p>
            <ul>
                <li><a href="https://intranet.alxswe.com/rltoken/jf71oYqiETchcVhPzQVnyg"> WHAT IS PII, non-PII and Personal Data</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/W2JiHD6cbJY1scJORyLqnw">logging documentation</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/41oaQXfzwnF1i-wT8W0vHw">bcrypt package</a></li>
                <li><a href="https://intranet.alxswe.com/rltoken/XCpI9uvguxlTCsAeRCW6SA">Logging to Files, Setting Levels, and Formatting</a></li>
            </ul>
        </p>
        <h2> KNOWLEDGE CHECK</h2>
        <p>
            <ul>
                <li>Examples of Personally Identifiable information (PII)</li>
                <li>How to implement a log filter that will obfuscate PII fields></li>
                <li>How to encrypt a password and check the validity of an input password></li>
                <li>How to authenticate to a database using environment variables  ></li> 
            </ul> 
        </p>
        <h3>What Is PII, non-PII, and Personal Data?</h3> 
        <p>
            <h4>What is personally identifiable information (PII)?</h4>
            <p> 
                PII is information that can be used to identify an individual. It is data that can be used to identify an individual. This data includes name,
                This data include name, address, phone number, email, social security number, date of birth, and any other information that can be used to identify an individual.<br>
            </p>
            <h4>What pieces of information are considered PII?</h4>
            <p>
                it can be divided into <code>linked</code> and <code>linkable</code> information. <br>
                <br>
                <code>Linked</code> information is information that can be used to link the information to an individual. <br>
                It includes name, address, phone number, email, social security number, date of birth, and any other information that can be used to link the information to an individual.<br>
                <code>Linkable information</code> is indirect, and can be combined with another information to link the information to an individual. <br>
                It includes first or last name, country, state , cit, zip code, gender, race, agge range, job position or workplace                
            </p>
            <h4>What is non-PII?</h4>
            <p>
                non-PII is information that cannot be used to identify an individual on its own<br>. This data includes cooki IDs, deviceIDs<br>
            </p>
            <hr> 
            <br>
            <h4>What is personal data?</h4>
            <p>personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person; <br>
            Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identification tags. This may leave traces which, in particular when combined with unique identifiers and other information received by the servers, may be used to create profiles of the natural persons and identify them. <br>
            This include informatonlike: TRANSACTION HISTORY, IP ADDRESS, browser history, posts on soial media
            </p>
            <h4>What is non-personal data?</h4>
            <p> he principles of data protection should therefore not apply to anonymous information, namely information which does not relate to an identified or identifiable natural person or to personal data rendered anonymous in such a manner that the data subject is not or no longer identifiable. <br>
            This include age range, statistic
            </p>
        </p>
    </body>    
</html>
