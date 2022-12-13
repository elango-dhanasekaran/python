     
var p = context.getVariable("proxy.pathsuffix");
var env = context.getVariable("environment.name");
var source = p;
print(p);
var services = p.split('/')[1];

print(services);
var urlParts = source.split("/");
var id = "/" + urlParts[urlParts.length - 1];
//new_target_pathsuffix = newPathSuffix + id + req_querystring;
   
 var source = '/'+urlParts[3]+ '/'+ urlParts[4]+ '/'+ urlParts[5];
 context.setVariable("source",source);
print(source);
if (env == "dev"){
if (services == "caas")
    {
    source = p.replace("caas","caas-dev");
    }
else if (services == "digitsOrchestratorService")
    {
    source = p.replace("digitsOrchestratorService","digitsOrchestratorService-dev");
    }
else if (services == "digitsNotificationService")
    {
    source = p.replace("digitsNotificationService","digitsNotificationService-dev");
    }
else if (services == "daasmstoresync")
    {
    source = p.replace("daasmstoresync","daasmstoresync-dev");
    }
else if (services == "digitslink")
    {
    source = p.replace("digitslink","digitslink-dev");
    }
else{
    source = p;
    }
}
print(source);

context.setVariable("targetPath", source);

// //  var clientId = context.getVariable('target.url');
// var targeturl = context.getVariable("targetPath");
// var test= context.getVariable("target.url");
// var test1= context.getVariable("target.pathsuffix");
// var test2= context.getVariable("target.basepath");


//  var host = context.getVariable("target.url");
//  var suffix = context.getVariable("proxy.pathsuffix");
 
 
//  context.setVariable("targetPath","/newURL");
//  var targeturl = context.getVariable("targetPath","/newURL");

 
// //var suffix = context.setVariable("proxy.pathsuffix");