CREATE TABLE LabMember
        (name VARCHAR(30) NOT NULL PRIMARY KEY,
         contactInformation VARCHAR(15),
         status VARCHAR(8));

CREATE TABLE Researcher 
        (name VARCHAR(30) NOT NULL PRIMARY KEY,
         levels VARCHAR(10) NOT NULL,
         FOREIGN KEY(name) REFERENCES LabMember);
    
CREATE TABLE ResearchAssistant
        (name VARCHAR(30) NOT NULL PRIMARY KEY,
         FOREIGN KEY(name) REFERENCES LabMember);
         
CREATE TABLE CLicDashboard
        (dID INT NOT NULL PRIMARY KEY,
         dates DATE,
         paths VARCHAR(50),
         focus FLOAT,
         SNR FLOAT,
         contaminants INT,
         crID INT NOT NULL,
         name VARCHAR(30) NOT NULL,
         FOREIGN KEY(crID) REFERENCES CLiCRawData,
         FOREIGN KEY(name) REFERENCES ResearchAssistant);
         
CREATE TABLE NanoparticleAnalysisResults
        (narID INT NOT NULL PRIMARY KEY,
         dates DATE,
         paths VARCHAR(50),
         avgRadius float,
         crID INT NOT NULL,
         name VARCHAR(30) NOT NULL,
         FOREIGN KEY(crID) REFERENCES NanoparticleData,
         FOREIGN KEY(name) REFERENCES ResearchAssistant);

CREATE TABLE BindingAnalysisResults
        (barID INT NOT NULL PRIMARY KEY,
         dates DATE,
         paths VARCHAR(50),
         analysisType VARCHAR(9),
         crID INT NOT NULL,
         name VARCHAR(30) NOT NULL,
         FOREIGN KEY(crID) REFERENCES DNAUnwindingData,
         FOREIGN KEY(name) REFERENCES ResearchAssistant);

CREATE TABLE CLiCRawData
        (crID INT NOT NULL PRIMARY KEY,
         dates DATE,
         paths VARCHAR(50));

CREATE TABLE NanoparticleData
        (crID INT NOT NULL PRIMARY KEY,
         FOREIGN KEY(crID) REFERENCES CLiCRawData);
         
CREATE TABLE DNAUnwindingData
        (crID INT NOT NULL PRIMARY KEY,
         FOREIGN KEY(crID) REFERENCES CLiCRawData);

CREATE TABLE Protocol
        (protocolID INT NOT NULL PRIMARY KEY,
         paths VARCHAR(50),
         name VARCHAR(30) NOT NULL,
         FOREIGN KEY(name) REFERENCES Researcher);

CREATE TABLE Microscope
        (microscopeID VARCHAR(7) NOT NULL PRIMARY KEY,
         status VARCHAR(8));

CREATE TABLE Experiment
        (protocolID INT NOT NULL,
         tryNumber INT NOT NULL,
         microscopeID VARCHAR(7) NOT NULL,
         crID INT,
         name VARCHAR(30),
         PRIMARY KEY(protocolID, tryNumber),
         FOREIGN KEY(protocolID) REFERENCES Protocol,
         FOREIGN KEY(microscopeID) REFERENCES Microscope,
         FOREIGN KEY(crID) REFERENCES CliCRawData,
         FOREIGN KEY(name) REFERENCES Researcher);

CREATE TABLE Supervise
        (startDate DATE NOT NULL,
         endDate DATE,
         rName VARCHAR(30) NOT NULL,
         raName VARCHAR(30) NOT NULL UNIQUE,
         PRIMARY KEY(rName, raName),
         FOREIGN KEY(rName) REFERENCES Researcher,
         FOREIGN KEY(raName) REFERENCES ResearchAssistant);
         
