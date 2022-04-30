import { Chip, Link } from "@mui/material";
import Grid from "@mui/material/Grid";
import MUIDataTable from "mui-datatables";
import { Link as RouterLink } from "react-router-dom";
import Page from "../common/Page";
import { displayTextWithTooltipForTruncated } from "../common/util";
import dailyDeliveries from "../data/daily_delivery.json";

function getPacksSummary(packs) {
  return packs.length > 0
    ? packs[packs.length - 1].summary.map((s) => s.name)
    : [];
}

function DailyDeliveryTable() {
  const data = dailyDeliveries.map((delivery) => [
    delivery.name,
    delivery.packs.length,
    getPacksSummary(delivery.packs),
  ]);

  return (
    <Page title="Daily Deliveries">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12}>
          <MUIDataTable
            title="Daily Delivery Pack List"
            data={data}
            columns={[
              {
                name: "Name",
                options: {
                  sort: false,
                  customBodyRenderLite: (dataIndex) => {
                    const id = dailyDeliveries[dataIndex].id;
                    const title = data[dataIndex][0];
                    return displayTextWithTooltipForTruncated(
                      title,
                      (text) => (
                        <Link
                          component={RouterLink}
                          to={`/daily-delivery/${id}`}
                        >
                          {text}
                        </Link>
                      ),
                      30
                    );
                  },
                },
              },
              { name: "# of Tiers", options: { sort: false } },
              {
                name: "Summary",
                options: {
                  sort: false,
                  customBodyRenderLite: (dataIndex) => {
                    const value = data[dataIndex][2];
                    return value.map((val, key) => {
                      return displayTextWithTooltipForTruncated(val, (text) => (
                        <Chip label={text} key={key} />
                      ));
                    });
                  },
                },
              },
            ]}
            options={{
              download: false,
              filter: false,
              print: false,
              jumpToPage: true,
              sort: false,
              selectableRows: "none",
              storageKey: "daily-delivery-table-state",
            }}
          />
        </Grid>
      </Grid>
    </Page>
  );
}

export default DailyDeliveryTable;
