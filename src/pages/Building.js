import Grid from "@mui/material/Grid";
import Page from "../common/Page";
import buildings from "../data/building.json";
import BuildingCard from "./BuildingCard";

function Building() {
  buildings = buildings.sort((a, b) => b.levels.length - a.levels.length);
  return (
    <Page title="Buildings">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        {buildings.map((building) => {
          return (
            <Grid item xs={12} md={6} lg={4} key={building.id}>
              <BuildingCard building={building} />
            </Grid>
          );
        })}
      </Grid>
    </Page>
  );
}

export default Building;
