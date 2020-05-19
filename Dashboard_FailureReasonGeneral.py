import aws
import re
import datetime
from datetime import timedelta, date


trials = aws.downloadAllSessions(None, True)

count=0
s=[]
FailurReasonHistogram=dict()
d=None
for i in trials:
    a = trials[i]
    for b in a:
        c = a[b]
    for KWs in c:
        if KWs == 'failError':
            d = c['failError']
            FailureReason = re.findall('[a-zA-Z]+_[0-9]', d)
            #print(FailureReason)
            #count = count + 1
            #print(count)
            s.extend(FailureReason)
            for SingleFailure in FailureReason:
                FailurReasonHistogram[SingleFailure]=FailurReasonHistogram.get(SingleFailure,0)+1
            

#print(s)
print(FailurReasonHistogram)      
    