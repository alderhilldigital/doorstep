from .report import Report

class TabularReport(Report):

    preset = 'tabular'

    def add_issue(self, log_level, code, message, row_number=None, column_number=None, row=None):
        """This function will add an issue to the report and takes as parameters the processor, the log level, code, message"""

        if row_number:
            if column_number:
                typ = 'Cell'
            else:
                typ = 'Row'
        else:
            if column_number:
                typ = 'Column'
            else:
                typ = 'Global'

        item = {
            'entity': {
                'type': typ,
                'location': {
                    'row': row_number,
                    'column': column_number,
                },
                'definition': None
            },
            'properties': dict(row) if row else None
        }

        super(TabularReport, self).add_issue(log_level, code, message, item)