#!/usr/bin/env python
# -*- coding: utf-8 -*-

rating_files = ["2006jan", "2006apr", "2006jun", "2006okt", "2007jan", "2007mar", "2007jun", "2007sep", "2008jan", "2008apr", "2008jun", "2008sep", "2009jan", "2009apr", "2009jun", "2009sep", "2010jan", "2010apr", "2010jun", "2010sep", "2011jan", "2011apr", "2011jun", "2011sep", "2012jan", "2012apr", "2012jun", "2012sep", "2013jan", "2013apr", "2013jun", "2013sep", "2014jan", "2014apr", "2014jun", "2014sep", "2015jan", "2015apr", "2015jun", "2015sep"]

file_name = "ratingtall/" + rating_files[0] + ".txt"

f = open(file_name)

class RatingGraphObject:
    def __init__(self, line):
        self.full_name = line[6:32].strip()
        self.club = line[32:54].strip()
        self.temp_elo = line[54:61].strip().split(' ')[0]
        self.fide_elo = line[64:69].strip()

player = RatingGraphObject(f.readlines()[5])

dictplayer = player.__dict__

dictplayer["elos"] = {}

dictplayer["elos"][rating_files[0]] = dictplayer["temp_elo"]

def get_ratings_by_name(full_name):
  elo_dict = {}
  elo_dict["elos"] = []
  elo_dict["categories"] = []
  elo_dict["fide_elos"] = []

  for date in rating_files:
    file_name = "ratingtall/" + date + ".txt"

    f = open(file_name)

    line = None

    for l in f.readlines():
      if full_name in l:
        line = l
        break

    if line:
      line = line.replace(')', ' ')

      player = RatingGraphObject(line)

      dictplayer = player.__dict__

      elo_dict["categories"].append(date)
      elo_dict["elos"].append(int(dictplayer['temp_elo']))

      if not dictplayer['fide_elo'].isdigit():
        elo_dict["fide_elos"].append(None) 
      else:
        elo_dict["fide_elos"].append(int(dictplayer['fide_elo']))             

  return elo_dict["categories"], elo_dict["elos"], elo_dict["fide_elos"]

print get_ratings_by_name("Steinskog Asbjørn O.")