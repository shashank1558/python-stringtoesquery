# python-stringtoesquery
turn boolean expressions into elasticsearch queries

example:
```
>>> string_to_query('doctor and heart')
{'query': {'bool': {'should': [{'bool': {'must': [{'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': 'doctor',
                                                                   'type': 'phrase'}},
                                                  {'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': 'heart',
                                                                   'type': 'phrase'}}]}}]}}}
>>> string_to_query('"Tom and Jerry" or "Road runner and vil coyote"')
{'query': {'bool': {'should': [{'bool': {'must': [{'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': '"Tom '
                                                                            'and '
                                                                            'Jerry"',
                                                                   'type': 'phrase'}}]}},
                               {'bool': {'must': [{'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': '"Road '
                                                                            'runner '
                                                                            'and '
                                                                            'vil '
                                                                            'coyote"',
                                                                   'type': 'phrase'}}]}}]}}}
>>> string_to_query('cat and cat food or dog and dog food')
{'query': {'bool': {'should': [{'bool': {'must': [{'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': 'cat',
                                                                   'type': 'phrase'}},
                                                  {'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': 'cat '
                                                                            'food',
                                                                   'type': 'phrase'}}]}},
                               {'bool': {'must': [{'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': 'dog',
                                                                   'type': 'phrase'}},
                                                  {'multi_match': {'fields': ['Review.Text',
                                                                              'Review.Title'],
                                                                   'query': 'dog '
                                                                            'food',
                                                                   'type': 'phrase'}}]}}]}}}
```
