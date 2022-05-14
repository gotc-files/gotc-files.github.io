import { Slider, Typography } from "@mui/material";
import Grid from "@mui/material/Grid";
import { Box } from "@mui/system";
import useLocalStorage from "@rehooks/local-storage";
import DataTable from "../common/DataTable";
import Page from "../common/Page";
import heroCollectionActions from "../data/hero_collection_action.json";

function HeroCollectionAction() {
  const [currentCollectionLevel, setCurrentCollectionLevel] = useLocalStorage(
    "hero-collection-action-level",
    heroCollectionActions.hero_stars_requirement.length
  );
  const index = currentCollectionLevel - 1;

  return (
    <Page title="Hero Collection Actions">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12}>
          <DataTable
            title={
              <Box sx={{ py: 2 }}>
                <Typography variant="h6">
                  Hero Collection Actions Level {currentCollectionLevel} (
                  {heroCollectionActions.hero_stars_requirement[index]} Stars)
                </Typography>
                <Slider
                  defaultValue={
                    heroCollectionActions.hero_stars_requirement.length
                  }
                  valueLabelDisplay="auto"
                  step={1}
                  min={1}
                  max={heroCollectionActions.hero_stars_requirement.length}
                  value={currentCollectionLevel}
                  sx={{ color: "primary.main" }}
                  onChange={(e, newValue) => {
                    setCurrentCollectionLevel(newValue);
                  }}
                />
              </Box>
            }
            storageKey="hca-state"
            data={heroCollectionActions.actions}
            searchKeyAccessor={(action) => [action.name, action.description]}
            columnConfigs={[
              {
                name: "Name",
                valueType: "text",
                valueAccessor: (action) => action.name,
                tooltipAccessor: (action) =>
                  action.num_uses
                    ? action.description.replace("{0}", action.num_uses[index])
                    : action.description,
              },
              {
                name: "Level",
                valueType: "number",
                valueAccessor: (action) => action.level[index],
              },
              {
                name: "Type",
                valueType: "text",
                valueAccessor: (action) => action.tag,
                filter: true,
              },
              {
                name: "Stat Name",
                valueType: "text",
                valueAccessor: (action) => action.stat.name,
                tooltipAccessor: (action) => action.stat.description,
              },
              {
                name: "Stat Value",
                valueType: "stats",
                valueAccessor: (action) => action.buff[index],
              },

              {
                name: "Cooldown",
                valueType: "time",
                valueAccessor: (action) => action.cooldown[index],
              },
              {
                name: "Duration",
                valueType: "time",
                valueAccessor: (action) => action.duration[index],
              },
              {
                name: "Influence Cost",
                valueType: "number",
                valueAccessor: (action) => action.influence_cost[index],
              },
              {
                name: "Num Uses",
                valueType: "text",
                valueAccessor: (action) =>
                  action.num_uses ? action.num_uses[index] : "N/A",
              },
            ]}
            options={{
              rowsPerPage: 20,
              rowsPerPageOptions: [],
              jumpToPage: false,
              filter: true,
              filterType: "checkbox",
            }}
          />
        </Grid>
      </Grid>
    </Page>
  );
}

export default HeroCollectionAction;
