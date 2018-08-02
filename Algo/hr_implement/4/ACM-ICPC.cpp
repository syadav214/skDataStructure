/*There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. 
Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person team can know.
 Also find out how many ways a team can be formed to know that many topics. Lists will be in the form of bit strings, 
where each string represents an attendee and each position in that string represents a field of knowledge, 1 if its a known field or 0 if not.
*/

#include <iostream>
#include <vector>
using namespace std;

vector<int> acmTeam(vector<string> topic)
{
    vector<int> result;
    int len = topic.size();
    int known, max_known = 0, know_all = 0;

    for (int i = 0; i < len; i++)
    {
        for (int j = i + 1; j < len; j++)
        {
            known = 0;
            for (int k = 0; k < topic[i].size(); k++)
            {
                if (topic[i][k] == '1' || topic[j][k] == '1')
                    known++;

                if (known > max_known)
                {
                    max_known = known;
                    know_all = 0;
                }

                if (known == max_known)
                    know_all++;
            }
        }
    }

    cout << max_known << endl;
    cout << know_all << endl;
    result.push_back(max_known);
    result.push_back(know_all);

    return result;
}

int main()
{
    vector<string> topic;
    topic.push_back("10101");
    topic.push_back("11100");
    topic.push_back("11010");
    topic.push_back("00101");
    acmTeam(topic);
    return 0;
}
