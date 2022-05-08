import useLocalStorage from "@rehooks/local-storage";
import DataCard from "../common/DataCard";

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

const RARITY_TO_COLOR_NAME = {
  1: "common.main",
  2: "fine.main",
  3: "exquisite.main",
  4: "epic.main",
};

function HeroCard(props) {
  const [heroLevel, setHeroLevel] = useLocalStorage(
    `${formatHeroIdentifier(props.hero)}-level`,
    props.hero.max_stars * 10
  );

  return (
    <DataCard
      title={`${props.hero.name} (${heroLevel})`}
      subtitle={props.hero.description}
      color={RARITY_TO_COLOR_NAME[props.hero.rarity]}
      slider={{
        min: 1,
        max: Math.max(props.hero.max_stars * 10),
        value: heroLevel,
        setValue: setHeroLevel,
      }}
      data={props.hero.skills
        .filter((skill) => heroLevel >= (skill.unlock_level || 0))
        .map((skill) => ({
          name: `(${skill.type.charAt(0)}) ${skill.name}`,
          tooltip: skill.description,
          value: heroSkillValue(skill, heroLevel - 1),
        }))}
    />
  );
}

export default HeroCard;
