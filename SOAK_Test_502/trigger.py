import SOAK_Test_502.createEntity
import SOAK_Test_502.logInToZDP
import SOAK_Test_502.createWorkflow
import SOAK_Test_502.createLZDirectory
import SOAK_Test_502.fetchConnections
import SOAK_Test_502.createFilePattern
import SOAK_Test_502.createDQRule
import time
import SOAK_Test_502.remoteConnection
print("Log into ZDP...")
session=SOAK_Test_502.logInToZDP.logIn()
print("Create DQ Rule....")
ruleId,ruleName=SOAK_Test_502.createDQRule.createDQRule(session)
print("DQ Rule ID:  ",ruleId,"DQ Rule Name:  ",ruleName)
print(".................................")
print("Create Entity.....")
entityTypeId,version,entityName=SOAK_Test_502.createEntity.createEntity(session,ruleId,ruleName)
print("Entity type ID:  ",entityTypeId,"Entity version:  ",version,"Entity Name:  ",entityName)
print("-------------------------------------")
print("Create Connection.....")
connection_id=SOAK_Test_502.fetchConnections.fetch_connections(session)
print("Connection ID:  ",connection_id)
print("--------------------------------------")
print("Create Workflow....")
wfId=SOAK_Test_502.createWorkflow.createWorkflow(session,entityTypeId,version,entityName,connection_id)
print("Workflow created ID:  ",wfId)
print("-------------------------------------")
print("Fetch LZ server ID......")
serverId=SOAK_Test_502.createLZDirectory.fetchLZServers(session)
print("LZ Server ID:  ",serverId)
print("---------------------------------------")
print("Create LZ directory.....")
lzDirId,lzDirPath=SOAK_Test_502.createLZDirectory.createLZDir(session,serverId)
print("LZ directory ID:  ",lzDirId)
print("LZ direcotry created: ",lzDirPath)
print("--------------------------------------")
print("Create File Pattern......")
filePatternId=SOAK_Test_502.createFilePattern.createFilePattern(session,lzDirId,wfId,connection_id)
print("File pattern ID:  ",filePatternId)
print("---------------------------------------")
print("Sleeping for 10 seconds........")
time.sleep(10)
print("Trigger remote file droop script.....")
SOAK_Test_502.remoteConnection.remoteConnection(lzDirPath)
