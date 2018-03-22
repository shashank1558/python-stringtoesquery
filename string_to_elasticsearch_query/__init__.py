import re


class _ClauseParser:
    def __init__(self, tokenizer, *operators):
        self._tokenizer = tokenizer
        self._operators = set(op.lower() for op in operators)
        self._found_operator = None

    def __iter__(self):
        for token in self._tokenizer:
            token_value = token.group(0)
            operator = token.group(2)
            if operator is not None:
                operator = operator.lower()
            if operator in self._operators:
                self._found_operator = operator
                return
            yield token_value

    @property
    def operator(self):
        found_operator = self._found_operator
        self._found_operator = None
        return found_operator


def parse_raw_query(phrase):
    tokenizer = re.finditer(r'"([^"]+)"|(\w+)', phrase)
    clause_parser = _ClauseParser(tokenizer, 'and', 'or')
    current_group = []
    while True:
        current_group.append(' '.join(clause_parser))
        found_operator = clause_parser.operator
        if found_operator != 'and':
            yield current_group
            if found_operator is None:
                return
            current_group = []


def string_to_query(phrase, *fields):
    fields = [str(field) for field in fields]
    if not fields:
        raise ValueError(
                'at least one ElasticSearch field is '
                'required to search data into.')

    return {
            'query': {
                'bool': {'should': [
                    {
                        'bool': {'must': [
                            {'multi_match': {
                                'type': 'phrase',
                                'query': clause,
                                'fields': fields,
                            }} for clause in clauses
                        ]}
                    } for clauses in parse_raw_query(phrase)
                ]}
            }
    }
