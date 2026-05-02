#include <nlohmann/json.hpp>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string> 
using namespace std;
using json = nlohmann::json;

bool isBrowserApp(string className, string initialClass)
{
  if(className.find("chrome") != string::npos || initialClass.find("chrome") != string::npos) return true; 
  else if(className.find("chromium") != string::npos || initialClass.find("chromium") != string::npos) return true; 
  

  return false;
}

int main()
{
  string path = "/home/ysuovnii/.config/hyprrestore/snapshots/snapshot.json";
  ifstream file(path);
  if(!file)
  {
    cerr << "Failed to Restore\n";
    return 1;
  }

  json data;
  file >> data;

  for(int i = 0; i < data.size(); i++)
  {
    string app = data[i]["class"];
    string initialClass = data[i]["initialClass"];
    string initialTitle = data[i]["initialTitle"];
    string script;
    
    if(isBrowserApp(app, initialClass)) 
    {
      string site = "https://" + initialTitle + "";
      script = "xdg-open \"" + site + "\"";
    }
    else script = app + " &";

    
    int status = system(script.c_str());
    if(status != 0)
    {
      cout << "script : " << script << "endl";
      cerr << "Failed to start " << app << endl;
    }
  }

  return 0;
}
