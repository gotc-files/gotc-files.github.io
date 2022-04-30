import Grid from "@mui/material/Grid";
import useLocalStorage from "@rehooks/local-storage";
import DataCard from "../common/DataCard";
import Page from "../common/Page";
import enhancements from "../data/enhancement.json";

function EnhancementCard(props) {
  const enhancement = props.enhancement;
  const levels = enhancement.levels.map(
    (enhancementLevel) => enhancementLevel.level
  );
  const [level, setLevel] = useLocalStorage(
    `enhancement-level-${enhancement.name.replaceAll(" ", "-").toLowerCase()}`,
    Math.max(...levels)
  );
  const enhancementLevel = enhancement.levels.find(
    (enhancementLevel) => enhancementLevel.level === level
  );
  const data = [
    {
      name: "Event Score",
      value: enhancementLevel.event_score,
      valueType: "number",
    },
    {
      name: "Power",
      value: enhancementLevel.power,
      valueType: "number",
    },
    {
      name: `(Stat) ${enhancement.stat.name}`,
      tooltip: enhancement.stat.description,
      value: enhancementLevel.stat,
    },
    {
      name: "Upgrade Time",
      value: enhancementLevel.upgrade_time_seconds,
      valueType: "time",
    },
  ];
  data.push(
    ...enhancementLevel.costs
      .filter((cost) => cost.cost > 0)
      .map((cost) => ({
        name: `(Cost) ${cost.name}`,
        tooltip: cost.description,
        value: cost.cost,
        valueType: "number",
      }))
  );
  return (
    <DataCard
      title={`${enhancement.name} (${level})`}
      subtitle={enhancement.stat.name}
      color="primary.main"
      slider={
        levels.length > 1 && {
          min: Math.min(...levels),
          max: Math.max(...levels),
          value: level,
          setValue: setLevel,
        }
      }
      data={data}
    />
  );
}

function Enhancement() {
  return (
    <Page title="Enhancements">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        {enhancements.map((enhancement) => {
          return (
            <Grid item xs={12} md={6} lg={4} key={enhancement.id}>
              <EnhancementCard enhancement={enhancement} />
            </Grid>
          );
        })}
      </Grid>
    </Page>
  );
}

export default Enhancement;
