#include <nlohmann/json.hpp>
#include <cstdio>
#include <fstream>
#include <iostream>
using namespace std;
using json = nlohmann::json;

int main()
{
  string path = "/home/ysuovnii/.config/snapshots/snapshot.json";
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
    string script = app + " &";
    
    int status = system(script.c_str());
    if(status != 0)
    {
      cerr << "Failed to start " << app << endl;
    }
  }

  return 0;
}
