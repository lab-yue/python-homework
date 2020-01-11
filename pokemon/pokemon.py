import json
import statistics

with open('./data/data/pokemon_data.json') as f:
  pokemon_data = json.loads(f.read())

ranks = sorted(pokemon_data, key=lambda pokemon: -pokemon.get('stats').get('attack'))

for rank in ranks[:3]:
  print(json.dumps(rank, indent=4, ensure_ascii=False))

speed_avg = statistics.mean([pokemon.get('stats').get('speed') for pokemon in pokemon_data])

#print(speed_avg)

def can_be_firefighter(no:int):

  def is_ok(pokemon):
    if(pokemon.get('no') != no):
      return False
    if (pokemon.get('stats').get('speed') <= speed_avg):
      return False
    if ("みず" not in pokemon.get('types')):
      return False
    return True

  if pokemon := next(filter(is_ok,pokemon_data)):
    print(pokemon)
    return

can_be_firefighter(419)

defence_median = statistics.median([pokemon.get('stats').get('defence') for pokemon in pokemon_data])

def get_defence(pokemon):
  return pokemon.get('stats').get('defence')

def check_pokemon_2(no:int):

  for pokemon in pokemon_data:
    if pokemon.get('no') == no and get_defence(pokemon) > defence_median and "でんき" in pokemon.get('types'):
      print(pokemon)
      return
#check_pokemon_2(26)