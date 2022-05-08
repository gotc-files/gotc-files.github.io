import Grid from "@mui/material/Grid";
import DataTable from "../common/DataTable";
import Page from "../common/Page";
import researches from "../data/research.json";

function aggregateOnLevels(research, valueAccessor, reducer, initialValue) {
  return research.levels
    .map((level) => valueAccessor(level))
    .reduce(reducer, initialValue);
}

function sumOnLevels(research, valueAccessor) {
  return aggregateOnLevels(
    research,
    valueAccessor,
    (previousValue, currentValue) => previousValue + currentValue,
    0
  );
}

function maxOnLevels(research, valueAccessor) {
  return aggregateOnLevels(
    research,
    valueAccessor,
    (previousValue, currentValue) => Math.max(previousValue, currentValue),
    0
  );
}

function lastOnLevels(research, valueAccessor) {
  return valueAccessor(research.levels[research.levels.length - 1]);
}

function ResearchTable() {
  return (
    <Page title="Researches">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12}>
          <DataTable
            title="Researches"
            storageKey="research-table-state"
            data={researches}
            searchKeysAccessor={(research) => [
              research.name,
              research.description,
            ]}
            columnConfigs={[
              {
                name: "Name",
                valueType: "text",
                valueAccessor: (research) => research.name,
                linkAccessor: (research) => `/research/${research.id}`,
                tooltipAccessor: (research) => research.description,
              },
              {
                name: "Category",
                valueType: "text",
                valueAccessor: (research) => research.category_name,
              },
              {
                name: "Levels",
                valueType: "number",
                valueAccessor: (research) => research.levels.length,
              },
              {
                name: "Stat Name",
                valueType: "text",
                valueAccessor: (research) =>
                  lastOnLevels(
                    research,
                    (level) => level.stats[level.stats.length - 1].name
                  ),
                tooltipAccessor: (research) =>
                  lastOnLevels(
                    research,
                    (level) => level.stats[level.stats.length - 1].description
                  ),
              },
              {
                name: "Stat Value",
                valueType: "stats",
                valueAccessor: (research) =>
                  lastOnLevels(
                    research,
                    (level) => level.stats[level.stats.length - 1].value
                  ),
              },
              {
                name: "Event Score",
                valueType: "number",
                valueAccessor: (research) =>
                  sumOnLevels(research, (level) => level.event_score),
              },
              {
                name: "Time",
                valueType: "time",
                valueAccessor: (research) =>
                  sumOnLevels(research, (level) => level.upgrade_time_seconds),
              },
              {
                name: "Power",
                valueType: "number",
                valueAccessor: (research) =>
                  maxOnLevels(research, (level) => level.power),
              },
            ]}
          />
        </Grid>
      </Grid>
    </Page>
  );
}

export default ResearchTable;
