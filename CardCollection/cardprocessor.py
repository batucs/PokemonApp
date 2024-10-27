from pokemonttcgsdk import Card

class CardProcessor:
    """A utility class that processes Pokémon TCG card types into a python type.

    This class provides static methods to process various attributes of Pokémon cards,
    including abilities, attacks, and subtypes, transforming them into a structured format
    for use in the application.

    Returns:
        None
    """

    @staticmethod
<<<<<<< Updated upstream
    def process_cards(cards):
        """
        Processes a list of Pokémon cards and 
        extracts relevant attributes.

        Args:
            cards (list[Card]): A list of Card objects 
            from the Pokémon TCG SDK.

        Returns:
            list[dict]: A list of dictionaries, each 
            containing processed information for a card, 
            including its abilities, attacks, and metadata.
        """
=======
    def process_cards(
        cards: list,
        include_id: bool = True,
        include_name: bool = True,
        include_supertype: bool = True,
        include_subtypes: bool = True,
        include_level: bool = True,
        include_hp: bool = True,
        include_types: bool = True,
        include_rules: bool = True,
        include_abilities: bool = True,
        include_attacks: bool = True,
        include_retreat_cost: bool = True,
        include_converted_retreat_cost: bool = True,
        include_set: bool = True,
        include_number: bool = True,
        include_artist: bool = True,
        include_rarity: bool = True,
        include_flavor_text: bool = True,
        include_images: bool = True,
    ) -> list[dict]:
>>>>>>> Stashed changes

        processed_cards = []
        for card in cards:
            processed_card = {
<<<<<<< Updated upstream
            **CardProcessor.process_abilities(card),
            **CardProcessor.process_attacks(card),
            **CardProcessor.process_subtypes(card),
            "name": card.name,
            "supertype": card.supertype,
            "imageUrl": card.images.large,
            "set": card.set.name,
            "setSymbol": card.set.images.symbol,
            "setLogo": card.set.images.logo,
=======
                **(CardProcessor.process_abilities(card) if include_abilities else {}),
                **(CardProcessor.process_attacks(card) if include_attacks else {}),
                **(CardProcessor.process_subtypes(card) if include_subtypes else {}),
                **(CardProcessor.process_types(card) if include_types else {}),

                "id": card.id if include_id else None,
                "name": card.name if include_name else None,
                "supertype": card.supertype if include_supertype else None,
                "hp": card.hp if include_hp else None,
                "types": card.types if include_types else [],
                "rules": card.rules if include_rules else [],
                "retreatCost": card.retreatCost if include_retreat_cost else [],

                "convertedRetreatCost": (
                card.convertedRetreatCost if
                    include_converted_retreat_cost else 0
                ),

                "set": card.set.name if include_set else None,
                "number": card.number if include_number else None,
                "artist": card.artist if include_artist else None,
                "rarity": card.rarity if include_rarity else None,
                "flavorText": card.flavorText if include_flavor_text else None,
                "imageUrl": card.images.large if include_images else None,

                "setSymbol": card.set.images.symbol
                if include_images and include_set
                else None,

                "setLogo": card.set.images.logo
                if include_images and include_set
                else None,
>>>>>>> Stashed changes
            }

            processed_cards.append(processed_card)

        return processed_cards

    @staticmethod
    def process_abilities(card):
        """
        Extracts abilities from a Pokémon card.

        Args:
            card (Card): A Card object from the Pokémon TCG SDK.

        Returns:
            dict: A dictionary containing the first two abilities 
            of the card, if available, along with their names, 
            text descriptions, and types.
        """

        abilities = {
            "ability1Name": "",
            "ability1Text": "",
            "ability1Type": "",
            "ability2Name": "",
            "ability2Text": "",
            "ability2Type": "",
        }

<<<<<<< Updated upstream
        # Check if abilities exists and is not None
        if hasattr(card, 'abilities') and card.abilities:  
            if len(card.abilities) > 0:

                abilities["ability1Name"] = card.abilities[0].name                

                abilities["ability1Text"] = \
                    card.abilities[0].text if hasattr(card.abilities[0], 'text') else ""

                abilities["ability1Type"] = \
                    card.abilities[0].type if hasattr(card.abilities[0], 'type') else ""

=======
        if (
            hasattr(card, "abilities") and card.abilities
        ):  # Check if abilities exists and is not None
            if len(card.abilities) > 0:
                abilities["ability1Name"] = card.abilities[0].name
                abilities["ability1Text"] = (
                    card.abilities[0].text if hasattr(card.abilities[0], "text") else ""
                )
                abilities["ability1Type"] = (
                    card.abilities[0].type if hasattr(card.abilities[0], "type") else ""
                )
>>>>>>> Stashed changes
            if len(card.abilities) > 1:

                abilities["ability2Name"] = card.abilities[1].name
<<<<<<< Updated upstream

                abilities["ability2Text"] = card.abilities[1].text \
                    if hasattr(card.abilities[1], 'text') else ""

                abilities["ability2Type"] = card.abilities[1].type \
                    if hasattr(card.abilities[1], 'type') else ""
=======
                abilities["ability2Text"] = (
                    card.abilities[1].text if hasattr(card.abilities[1], "text") else ""
                )
                abilities["ability2Type"] = (
                    card.abilities[1].type if hasattr(card.abilities[1], "type") else ""
                )
>>>>>>> Stashed changes

        return abilities

    @staticmethod
    def process_attacks(card):
        """
        Extracts attack information from a Pokémon card.

        Args:
            card (Card): A Card object from the Pokémon TCG SDK.

        Returns:
            dict: A dictionary containing the first four attacks of the card, 
            if available, along with their costs, names, text descriptions, 
            damage values, and converted energy costs.
        """

        attacks = {}
<<<<<<< Updated upstream

        if hasattr(card, 'attacks') and card.attacks:  # Ensure attacks exists
=======
        if hasattr(card, "attacks") and card.attacks:  # Ensure attacks exists
>>>>>>> Stashed changes
            for i in range(4):

                attack_prefix = f"attack{i+1}"

                if len(card.attacks) > i:

                    attack = card.attacks[i]
<<<<<<< Updated upstream

                    cost = attack.cost if hasattr(attack, 'cost') and attack.cost else []

                    attacks.update({

                        f"{attack_prefix}Cost1": cost[0] if len(cost) > 0 else "",

                        f"{attack_prefix}Cost2": cost[1] if len(cost) > 1 else "",

                        f"{attack_prefix}Cost3": cost[2] if len(cost) > 2 else "",

                        f"{attack_prefix}Cost4": cost[3] if len(cost) > 3 else "",

                        f"{attack_prefix}Cost5": cost[4] if len(cost) > 4 else "",

                        f"{attack_prefix}Name": attack.name,

                        f"{attack_prefix}Text": attack.text if hasattr(attack, 'text') else "",

                        f"{attack_prefix}Damage": attack.damage \
                            if hasattr(attack, 'damage') else "",

                        f"{attack_prefix}ConvertedEnergyCost": attack.convertedEnergyCost \
                            if hasattr(attack, 'convertedEnergyCost') else 0
                    })
                else:

                    attacks.update({
=======
                    cost = (
                        attack.cost if hasattr(attack, "cost") and attack.cost else []
                    )
                    attacks.update(
                        {
                            f"{attack_prefix}Cost1": cost[0] if len(cost) > 0 else "",
                            f"{attack_prefix}Cost2": cost[1] if len(cost) > 1 else "",
                            f"{attack_prefix}Cost3": cost[2] if len(cost) > 2 else "",
                            f"{attack_prefix}Cost4": cost[3] if len(cost) > 3 else "",
                            f"{attack_prefix}Cost5": cost[4] if len(cost) > 4 else "",
                            f"{attack_prefix}Name": attack.name,
                            f"{attack_prefix}Text": attack.text
                            if hasattr(attack, "text")
                            else "",
                            f"{attack_prefix}Damage": attack.damage
                            if hasattr(attack, "damage")
                            else "",
                            f"{attack_prefix}ConvertedEnergyCost": attack.convertedEnergyCost
                            if hasattr(attack, "convertedEnergyCost")
                            else 0,
                        }
                    )
                else:
                    attacks.update(
                        {
                            f"{attack_prefix}Cost1": "",
                            f"{attack_prefix}Cost2": "",
                            f"{attack_prefix}Cost3": "",
                            f"{attack_prefix}Cost4": "",
                            f"{attack_prefix}Cost5": "",
                            f"{attack_prefix}Name": "",
                            f"{attack_prefix}Text": "",
                            f"{attack_prefix}Damage": "",
                            f"{attack_prefix}ConvertedEnergyCost": 0,
                        }
                    )
        else:
            # If attacks is None or empty, set defaults
            for i in range(4):
                attack_prefix = f"attack{i+1}"
                attacks.update(
                    {
>>>>>>> Stashed changes
                        f"{attack_prefix}Cost1": "",
                        f"{attack_prefix}Cost2": "",
                        f"{attack_prefix}Cost3": "",
                        f"{attack_prefix}Cost4": "",
                        f"{attack_prefix}Cost5": "",
                        f"{attack_prefix}Name": "",
                        f"{attack_prefix}Text": "",
                        f"{attack_prefix}Damage": "",
<<<<<<< Updated upstream
                        f"{attack_prefix}ConvertedEnergyCost": 0
                    })
        else:
            # If attacks is None or empty, set defaults
            for i in range(4):

                attack_prefix = f"attack{i+1}"

                attacks.update({
                    f"{attack_prefix}Cost1": "",
                    f"{attack_prefix}Cost2": "",
                    f"{attack_prefix}Cost3": "",
                    f"{attack_prefix}Cost4": "",
                    f"{attack_prefix}Cost5": "",
                    f"{attack_prefix}Name": "",
                    f"{attack_prefix}Text": "",
                    f"{attack_prefix}Damage": "",
                    f"{attack_prefix}ConvertedEnergyCost": 0
                })
=======
                        f"{attack_prefix}ConvertedEnergyCost": 0,
                    }
                )
>>>>>>> Stashed changes

        return attacks

    @staticmethod
<<<<<<< Updated upstream
    def process_subtypes(card):
        """
        Extracts subtypes from a Pokémon card.

        Args:
            card (Card): A Card object from the Pokémon TCG SDK.

        Returns:
            dict: A dictionary containing up to 
            four subtypes of the card, if available.
        """

        subtypes = {
            "subtype1": "",
            "subtype2": "",
            "subtype3": "",
            "subtype4": ""
        }
=======
    def process_types(card):
        types = {"type1": "", "type2": ""}
>>>>>>> Stashed changes

        if hasattr(card, "types") and card.types:  # Check if types exists
            if len(card.types) > 0:
                types["type1"] = card.types[0]  # First type
            if len(card.types) > 1:
                types["type2"] = card.types[1]  # Second type

        return types

    @staticmethod
    def process_subtypes(card):
        subtypes = {"subtype1": "", "subtype2": "", "subtype3": "", "subtype4": ""}

        if hasattr(card, "subtypes") and card.subtypes:  # Check if subtypes exists
            subtypes["subtype1"] = card.subtypes[0] if len(card.subtypes) > 0 else ""
            subtypes["subtype2"] = card.subtypes[1] if len(card.subtypes) > 1 else ""
            subtypes["subtype3"] = card.subtypes[2] if len(card.subtypes) > 2 else ""
            subtypes["subtype4"] = card.subtypes[3] if len(card.subtypes) > 3 else ""

        return subtypes
