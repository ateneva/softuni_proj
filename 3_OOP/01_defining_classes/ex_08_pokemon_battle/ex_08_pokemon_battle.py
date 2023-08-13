from dataclasses import dataclass


@dataclass
class Pokemon:
    name: str
    health: int

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


@dataclass
class Trainer:
    name: str
    pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        caught = [c for c in self.pokemon if c.name == pokemon_name]
        for c in caught:
            self.pokemon.remove(c)
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n" \
                 f"Pokemon count {len(self.pokemon)}\n"

        for p in self.pokemon:
            result += f"- {p.pokemon_details()}" + '\n'

        return result


pokemon = Pokemon("Pikachu", 90)

print(pokemon.pokemon_details())

trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))

second_pokemon = Pokemon("Charizard", 110)

print(trainer.add_pokemon(second_pokemon))

print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())