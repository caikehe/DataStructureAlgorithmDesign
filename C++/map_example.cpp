#include <iostream>
#include <map>
#include <string>
using namespace std;

typedef std::map<std::string, std::string> TStrStrMap;
typedef std::pair<std::string, std::string> TStrStrPair;

int main(int argc, char *argv[])
{
	TStrStrMap tMap;

	tMap.insert(TStrStrPair("yes", "no"));
	tMap.insert(TStrStrPair("up", "down"));
	tMap.insert(TStrStrPair("left", "right"));
	tMap.insert(TStrStrPair("good", "bad"));

	std::string s;
	std::cout << "Enter word: " << std::endl;;
	std::cin >> s;

	
	std::string strValue = tMap[s];
	if(strValue!="")
	{
		// Show value
		std::cout << "Opposite: " << strValue << endl;
	}
	else
	{
		TStrStrMap::iterator p;
		bool bFound=false;
		// Show key
		for(p = tMap.begin(); p!=tMap.end(); ++p)
		{
			std::string strKey;
			strValue = s;
			strKey= p->second;
			if( strValue  == strKey)
			{
				// Return key
				std::cout << "Opposite: " << p->first << std::endl;
				bFound = true;
			}
		}
		// If not found opposite word
		if(!bFound)
		{
			std::cout << "Word not in map." << std::endl;
		}
	}
	return 0;
}
