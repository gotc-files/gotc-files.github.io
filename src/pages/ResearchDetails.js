import { Grid } from "@mui/material";
import { useState } from "react";
import { useParams } from "react-router-dom";
import DataCard from "../common/DataCard";
import Page from "../common/Page";
import researches from "../data/research.json";

function ResearchCard(props) {
  const research = researches.find(
    (research) => research.id === props.researchId
  );
  const [currentLevel, setCurrentLevel] = useState(research.levels.length);

  const currentResearchLevel = research.levels.find(
    (researchLevel) => researchLevel.level === currentLevel
  );
  const data = [
    {
      name: "Event Score",
      value: currentResearchLevel.event_score,
      valueType: "number",
    },
    {
      name: "Power",
      value: currentResearchLevel.power,
      valueType: "number",
    },
    {
      name: "Time",
      value: currentResearchLevel.upgrade_time_seconds,
      valueType: "time",
    },
    {
      name: "(Requirement) Maester Tower",
      value: currentResearchLevel.building_level_requirement,
      valueType: "number",
    },
  ];
  if (currentResearchLevel.dragon_pit_requirement) {
    data.push({
      name: "(Requirement) Dragon Pit Level",
      value: currentResearchLevel.dragon_pit_requirement,
      valueType: "number",
    });
  }
  if (currentResearchLevel.dragon_requirement) {
    data.push({
      name: "(Requirement) Dragon Level",
      value: currentResearchLevel.dragon_requirement,
      valueType: "number",
    });
  }
  data.push(
    ...research.requirements.map((requirement) => ({
      name: `(Requirement) ${requirement.name}`,
      value: requirement.level,
      valueType: "number",
      link: `/research/${requirement.id}`,
    }))
  );
  data.push(
    ...currentResearchLevel.costs
      .filter((cost) => cost.cost > 0)
      .map((cost) => ({
        name: `(Cost) ${cost.name}`,
        tooltip: cost.description,
        value: cost.cost,
        valueType: "number",
      }))
  );
  data.push(
    ...currentResearchLevel.stats.map((stat) => ({
      name: `(Stat) ${stat.name}`,
      tooltip: stat.description,
      value: stat.value,
    }))
  );
  return (
    <DataCard
      title={`${research.name} (${currentLevel})`}
      subtitle={research.description}
      color="primary.main"
      slider={
        research.levels.length > 1
          ? {
              min: 1,
              max: research.levels.length,
              value: currentLevel,
              setValue: setCurrentLevel,
            }
          : null
      }
      data={data}
    />
  );
}

function ResearchDetails() {
  const { researchId } = useParams();

  return (
    <Page title="Research" backLink="/research">
      <Grid
        container
        spacing={2}
        sx={{ px: 0, py: 2 }}
        alignItems="center"
        justifyContent="center"
      >
        <Grid item xs={12} md={8} sx={{ p: 0 }}>
          <ResearchCard key={researchId} researchId={researchId} />
        </Grid>
      </Grid>
    </Page>
  );
}

export default ResearchDetails;
