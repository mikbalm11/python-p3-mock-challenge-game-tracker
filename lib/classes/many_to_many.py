from statistics import mean

class Game:
    
    all = []
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)
        
    @property
    def title(self): 
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, "title"):
            self._title = title
        else:
            raise Exception("Title must be a non-empty string.")

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        scores = [result.score for result in player.results() if result.game is self]
        return mean(scores) if len(scores) else 0

class Player:
    
    all = []
    def __init__(self, username):
        self.username = username
        type(self).all.append(self)
        
    @property
    def username(self): 
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) > 1 and len(username) < 17:
            self._username = username
        else:
            raise Exception("Username must be a non-empty string.")

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return [result.game for result in self.results()].count(game)

class Result:
    
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and score > 0 and score < 5001 and not hasattr(self, "score"):
            self._score = score
        elif score > 0 and score < 5001:
            raise Exception("Score must be a non-negative integer.")
        else:
            raise Exception("Score must be between 1 and 5000 inclusive.")
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Player must be an instance of Player.")
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Game must be an instance of Game.")
