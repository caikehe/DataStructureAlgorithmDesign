#include <iostream>
#include <vector>

using namespace std;

main()
{
   vector< vector<int> > vI2Matrix;    // Declare two dimensional array
   vector<int> A, B;
   vector< vector<int> >::iterator iter_ii;
   vector<int>::iterator                 iter_jj;

   A.push_back(10);
   A.push_back(20);
   A.push_back(30);
   B.push_back(100);
   B.push_back(200);
   B.push_back(300);

   vI2Matrix.push_back(A);
   vI2Matrix.push_back(B);

   cout << endl << "Using Iterator:" << endl;

   for(iter_ii=vI2Matrix.begin(); iter_ii!=vI2Matrix.end(); iter_ii++)
   {
      for(iter_jj=(*iter_ii).begin(); iter_jj!=(*iter_ii).end(); iter_jj++)
      {
         cout << (*iter_jj) << endl;
      }
   }
}
                
