import { Grid } from "@mui/material";
import { useState } from "react";
import { useParams } from "react-router-dom";
import DataCard from "../common/DataCard";
import Page from "../common/Page";
import { displayTruncated } from "../common/util";
import dailyDeliveries from "../data/daily_delivery.json";

function DailyDeliveryDetails() {
  const urlParams = useParams();
  const currentPackSet = dailyDeliveries.find(
    (packSet) => packSet.id === urlParams.packId
  );
  const tiers = currentPackSet.packs.map((pack) => pack.tier);
  const [tier, setTier] = useState(tiers[tiers.length - 1]);
  const pack = currentPackSet.packs.find((pack) => pack.tier === tier);
  return (
    <Page title="Daily Delivery" backLink="/daily-delivery">
      <Grid
        container
        spacing={2}
        sx={{ px: 0, py: 2 }}
        alignItems="center"
        justifyContent="center"
      >
        <Grid item xs={12} md={8} sx={{ p: 0 }}>
          <DataCard
            title={displayTruncated(currentPackSet.name, 30)}
            color="primary.main"
            select={{
              name: "pack-tier",
              choices: tiers,
              currentChoice: tier,
              handleChoiceChange: setTier,
            }}
            data={pack.items.map((item) => ({
              name: displayTruncated(item.name, 20),
              tooltip: item.description,
              value: item.quantity,
            }))}
          />
        </Grid>
      </Grid>
    </Page>
  );
}

export default DailyDeliveryDetails;
