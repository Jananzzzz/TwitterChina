# Decide whether a user have some relation to china

### Some considerations listed in order of importance from high to low with weighted score behind

1. the user's tweet (0.95)
if the user's tweet contains some chinese words, then the user obviously have some relation to china

2. the user's description (0.9)
if the user's description contains some chinese words, then the user obviously have some relation to china

3. the user's website or link (0.9)
if the user's website of link point to some chinese related info

4. the user's username (0.5)
based on deeplearning, if the user name contain chinese meaning, such as "dumpling, maozedong". Be careful with this feature.

5. the user's name (0.8)
need to rule out japanese users

6. the user'a location (0.9)
if the user's location is in china, then there is a high chance that the user have some relation to china.It obviously not be the opposite.

7. the user's profile image (0.5)
contain chinese words or chinese related images such as chinese flag or Tiananmen Square? or XI's images?

### Some other considerations:

1. main considerations' weight
2. taiwan users
3. what is the scope of "relation to china"?
4. how to deal with the users who have no tweet, no description, no name?
   for example, foreign users who randomly mentioned china?
   Users with a china profile?

### More to explore:
1. the connection in TwitterChina circle
  - divide them in different identity
  - divide them in different region
  - divide them in different circle
2. based on twitter recomendation algorithm and point 1, is it possible to predict the big events and trends?