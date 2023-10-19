test = {
  'name': 'Repr-esentation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class A:
          ...   def __init__(self, x):
          ...         self.x = x
          ...   def __repr__(self):
          ...         return self.x
          ...   def __str__(self):
          ...         return self.x * 2
          >>> class B:
          ...   def __init__(self):
          ...         print('boo!')
          ...         self.a = []
          ...   def add_a(self, a):
          ...         self.a.append(a)
          ...   def __repr__(self):
          ...         print(len(self.a))
          ...         ret = ''
          ...         for a in self.a:
          ...               ret += str(a)
          ...         return ret
          >>> A('one')
          498390232644b9ba9dd4de4e4067c8ec
          # locked
          >>> print(A('one'))
          a7fcd1c690cd1b9bf88e3478a317f435
          # locked
          >>> repr(A('two'))
          360366e8b533ac4eab6286ce9109b287
          # locked
          >>> b = B()
          d1a1c0f47a35c025d83ec8e75608c4a2
          # locked
          >>> b.add_a(A('a'))
          >>> b.add_a(A('b'))
          >>> b
          9338923f09aac77121029c604f7ce4f3
          385fe240900d010e992ca48877c08057
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
