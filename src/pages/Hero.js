import Grid from "@mui/material/Grid";
import useLocalStorage from "@rehooks/local-storage";
import MultiChoicesSelect from "../common/MultiChoicesSelect";
import Page from "../common/Page";
import heroes from "../data/hero.json";
import HeroCard from "./HeroCard";

const RARITY_NAMES = ["Uncommon", "Rare", "Heroic", "Mythic"];

function getAllTraits() {
  const traits = [...new Set(heroes.flatMap((hero) => hero.traits))];
  traits.sort();
  return traits;
}

function Hero() {
  const [selectedRarityIndices, setSelectedRarityIndices] = useLocalStorage(
    "hero-rarities",
    [2, 3]
  );

  const [selectedHeroTraits, setSelectedHeroTraits] = useLocalStorage(
    "hero-traits",
    []
  );

  const selectedHeroes = heroes
    .filter((hero) => selectedRarityIndices.includes(hero.rarity - 1))
    .filter(
      (hero) =>
        !selectedHeroTraits.length ||
        hero.traits.some((trait) => selectedHeroTraits.includes(trait))
    )
    .reverse();

  return (
    <Page title="Hero">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12} sx={{ p: 0 }}>
          <MultiChoicesSelect
            name="hero-rarity"
            choices={RARITY_NAMES}
            selectedChoices={selectedRarityIndices.map(
              (index) => RARITY_NAMES[index]
            )}
            handleChoicesChange={(selectedRarities) => {
              setSelectedRarityIndices(
                selectedRarities.map((rarity) => RARITY_NAMES.indexOf(rarity))
              );
            }}
          />
          <MultiChoicesSelect
            name="hero-traits"
            choices={getAllTraits()}
            selectedChoices={selectedHeroTraits}
            handleChoicesChange={(selectedHeroTraits) => {
              setSelectedHeroTraits(selectedHeroTraits);
            }}
          />
        </Grid>
        {selectedHeroes.map((hero) => (
          <Grid item xs={12} md={6} lg={4} key={hero.id}>
            <HeroCard hero={hero} />
          </Grid>
        ))}
      </Grid>
    </Page>
  );
}

export default Hero;
