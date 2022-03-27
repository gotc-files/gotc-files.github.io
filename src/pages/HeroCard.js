import { Card, CardContent, CardHeader } from "@mui/material";
import useLocalStorage from "@rehooks/local-storage";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import StatsTable from "../common/StatsTable";

const formatHeroIdentifier = (hero) => {
  return (hero.name + " " + hero.description)
    .split(" ")
    .map((word) => word.toLowerCase())
    .join("-");
};

const heroSkillValue = (skill, heroLevelIndex) => {
  if (skill.star_skill_value) {
    return skill.star_skill_value;
  }
  return skill.signature_skill_values[heroLevelIndex];
};

const RARITY_TO_COLOR = {
  1: "#6ad812",
  2: "#2892dc",
  3: "#d536db",
  4: "#fe7d0e",
};

function HeroCard(props) {
  const [heroLevel, setHeroLevel] = useLocalStorage(
    `${formatHeroIdentifier(props.hero)}-level`,
    props.hero.max_stars * 10
  );
  return (
    <Card>
      <CardHeader
        sx={{
          color: "white",
          backgroundColor: RARITY_TO_COLOR[props.hero.rarity],
        }}
        title={props.hero.name}
        titleTypographyProps={{ variant: "h6" }}
        subheader={props.hero.description}
        subheaderTypographyProps={{ color: "inherit" }}
      />
      <CardContent>
        <SingleChoiceSelect
          id={`${props.hero.id}-level`}
          name="hero-level"
          choices={[...Array(props.hero.max_stars * 10).keys()].map(
            (i) => i + 1
          )}
          currentChoice={heroLevel}
          handleChoiceChange={setHeroLevel}
        />
        <StatsTable
          stats={props.hero.skills.map((skill) => ({
            name: `(${skill.type.charAt(0)}) ${skill.name}`,
            description: skill.description,
            value: heroSkillValue(skill, heroLevel - 1),
          }))}
        />
      </CardContent>
    </Card>
  );
}

export default HeroCard;
