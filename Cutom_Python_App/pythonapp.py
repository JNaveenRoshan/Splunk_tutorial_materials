import sys
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration

@Configuration()
class pythonapp(StreamingCommand):
    def stream(self, records):
        for record in records:
            record['hello'] = 'orion'
            yield record

if __name__== "__main__":
        dispatch(pythonapp, sys.argv, sys.stdin, sys.stdout, __name__)

