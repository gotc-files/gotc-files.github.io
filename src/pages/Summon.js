import Grid from "@mui/material/Grid";
import { Navigate, useParams } from "react-router-dom";
import Page from "../common/Page";
import StatsCard from "../common/StatsCard";
import summons from "../data/summon.json";

const getSummonTimeStrName = (summon) => {
  return summon.time_str.toLowerCase() || "other";
};

const timeStrDisplay = (timeStrName) => {
  if (["other", "legacy_groups", "standard"].includes(timeStrName)) {
    return timeStrName
      .split("_")
      .map((word) => word[0].toUpperCase() + word.slice(1))
      .join(" ");
  }
  return (
    timeStrName[0].toUpperCase() +
    timeStrName.substr(1, 2) +
    " 20" +
    timeStrName.substr(3)
  );
};

const CATEGORY_TO_COLOR_NAME = {
  standard: "fine",
  noble: "exquisite",
  royal: "epic",
};

function Summon() {
  const urlParams = useParams();

  const timeStrNames = Array.from(
    new Set(summons.map(getSummonTimeStrName).reverse()).values()
  );
  if (!urlParams.timeStrName) {
    return <Navigate replace to={`/summon/${timeStrNames[0]}`} />;
  }
  const selectedSummons = summons.filter(
    (summon) => getSummonTimeStrName(summon) === urlParams.timeStrName
  );
  console.log(selectedSummons);

  return (
    <Page
      title="Summon"
      selectArgsList={[
        {
          name: "month",
          choices: timeStrNames.map((timeStrName) => ({
            id: timeStrName,
            name: timeStrDisplay(timeStrName),
            link: `/summon/${timeStrName}`,
          })),
          currentChoiceId: urlParams.timeStrName,
        },
      ]}
    >
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        {selectedSummons.map((summon) => (
          <Grid item xs={12} md={selectedSummons.length === 6 ? 4 : 3}>
            <StatsCard
              title={summon.heroes}
              subtitle={summon.name}
              color={CATEGORY_TO_COLOR_NAME[summon.category]}
              stats={summon.purchase_options[0].odds.map((odds) => ({
                name: `(${odds.quantity}x) ${odds.name}`,
                value: odds.probability,
                description: odds.description,
              }))}
            />
          </Grid>
        ))}
      </Grid>
    </Page>
  );
}

export default Summon;
