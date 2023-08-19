test = {
  'name': 'Question 4',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> hog_gcd(15, 25)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(13, 17)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(0, 5)
          26f5762c932a578994ea1c8fc7fa6c02
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(12, 64)
          4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(29, 79)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> hog_gcd(39, 627)
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(39)
          6593ddb13f56744fb8e2837aabae6ecb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(61)
          0e99a362b523f31de914b28a25f6599b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(50)
          a219d4eee1b4a0beae7bfbf59406dd04
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(100)
          100
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(1)
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(25)
          29
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(75)
          79
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_points(80)
          84
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 5, 7, make_test_dice(2, 4))
          ebb85ed86e75db9ccb48b9592f867cc1
          # locked
          >>> fuzzy_update(2, 5, 7, make_test_dice(2, 4)) # is 11 a fuzzy number?
          ebb85ed86e75db9ccb48b9592f867cc1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(0, 14, 27) # what happens when you roll 0 dice?
          1b69dde49f2d00e5909950f5df0efdd9
          # locked
          >>> fuzzy_update(0, 14, 27) # is 20 a fuzzy number?
          48ff0247787d837fbb51eaf221a5b30e
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> simple_update(2, 2, 3, make_test_dice(4))
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          >>> fuzzy_update(2, 2, 3, make_test_dice(4)) # is 10 a fuzzy number?
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(3, 11, 12, make_test_dice(4, 5, 6))
          26
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(2, 29, 17, make_test_dice(1, 3))
          30
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(0, 41, 42)
          60
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> fuzzy_update(2, 56, 56, make_test_dice(4))
          64
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> 'gcd' in dir() # do NOT import any new modules!
          False
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> import types
          >>> def imports():
          ...     for name, val in globals().items():
          ...         if isinstance(val, types.ModuleType):
          ...             yield val.__name__
          >>> list(imports()) # do NOT import any new modules!
          ['tests.construct_check', 'types']
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> test.check('hog.py', 'hog_gcd', ['Import', 'ImportFrom']) # do NOT import any new modules!
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
