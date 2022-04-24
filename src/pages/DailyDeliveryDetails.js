import { Card, CardContent, CardHeader, Grid } from "@mui/material";
import { useState } from "react";
import { useParams } from "react-router-dom";
import Page from "../common/Page";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import StatsTable from "../common/StatsTable";
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
          <Card>
            <CardHeader
              sx={{
                color: "white",
                backgroundColor: "primary.main",
              }}
              title={displayTruncated(currentPackSet.name, 30)}
              titleTypographyProps={{ variant: "h6" }}
            />
            <CardContent
              sx={{
                pt: 2,
                px: 1,
                pb: 0,
                "&:last-child": {
                  pb: 0.5,
                },
              }}
            >
              <SingleChoiceSelect
                name="pack-tier"
                choices={tiers}
                currentChoice={tier}
                handleChoiceChange={setTier}
              />
              <StatsTable
                stats={pack.items.map((item) => ({
                  name: displayTruncated(item.name, 20),
                  description: item.description,
                  value: item.quantity,
                }))}
              />
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </Page>
  );
}

export default DailyDeliveryDetails;
