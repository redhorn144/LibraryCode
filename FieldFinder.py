from pymarc import MARCReader
from pymarc import Record
from pymarc import XMLWriter
from pymarc import exceptions as exc

#if includes is True then the file will contain all of the records with the field given, and if False then all records without field given
def MarcFileSearch(field, filename, includes = True):
    reader = MARCReader(open(filename, 'rb'))

    # writing to a file
    writer = XMLWriter(open('file.xml','wb'))
    
    for record in reader:
        if record is None:
            print(
                "Current chunk: ",
                reader.current_chunk,
                " was ignored because the following exception raised: ",
                reader.current_exception
            )
        else:
            if len(record.get_fields(field)) == int(includes):
                writer.write(record)

    writer.close()




MarcFileSearch("245", 'metacoll.UIU.wcp.FIRM.YDX.D20231214.T213021.1.mrc')
                
