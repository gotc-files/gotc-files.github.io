import { CardContent } from "@mui/material";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import Grid from "@mui/material/Grid";
import useLocalStorage from "@rehooks/local-storage";
import React from "react";
import { Navigate, useParams } from "react-router-dom";
import Page from "../common/Page";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import StatsTable from "../common/StatsTable";
import trinketArmories from "../data/trinket_armory.json";

const LEVELS = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];
const TRINKET_ARMORY_COLLECTION_LEVELS = [...Array(150).keys()].map(
  (i) => i + 1
);

function TrinketArmory() {
  const urlParams = useParams();
  const [currentTrinketLevel, setCurrentTrinketLevel] = useLocalStorage(
    "trinket-level",
    40
  );
  const [currentQualityIndex, setCurrentQualityIndex] = useLocalStorage(
    "quality-index",
    2
  );
  const [currentTrinketArmoryLevelIndex, setCurrentTrinketArmoryLevelIndex] =
    useLocalStorage("trinket-armory-collection-level", 104);

  if (!urlParams.trinketArmoryId) {
    return (
      <Navigate
        replace
        to={`/trinket-armory/${trinketArmories[trinketArmories.length - 1].id}`}
      />
    );
  }

  const currentTrinktArmory = trinketArmories.find(
    (trinktArmory) => trinktArmory.id === urlParams.trinketArmoryId
  );
  return (
    <Page
      title="Trinket Armory"
      selectArgsList={[
        {
          name: "trinket-set",
          choices: trinketArmories.map((trinketArmory) => ({
            id: trinketArmory.id,
            name: trinketArmory.name,
            link: `/trinket-armory/${trinketArmory.id}`,
          })),
          currentChoiceId: urlParams.trinketArmoryId,
        },
      ]}
    >
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12} md={6} sx={{ p: 0 }}>
          <Card sx={{ color: "white" }}>
            <CardHeader
              title={currentTrinktArmory.name}
              style={{ backgroundColor: currentTrinktArmory.color }}
              subheaderTypographyProps={{ color: "inherit" }}
            />
            <CardContent>
              <SingleChoiceSelect
                name="level"
                choices={LEVELS}
                currentChoice={currentTrinketLevel}
                handleChoiceChange={setCurrentTrinketLevel}
              />
              <SingleChoiceSelect
                name="quality"
                choices={QUALITIES}
                currentChoice={QUALITIES[currentQualityIndex]}
                handleChoiceChange={(currentQuality) => {
                  setCurrentQualityIndex(
                    QUALITIES.findIndex((quality) => quality === currentQuality)
                  );
                }}
              />
              <SingleChoiceSelect
                name="armory-level"
                choices={TRINKET_ARMORY_COLLECTION_LEVELS}
                currentChoice={
                  TRINKET_ARMORY_COLLECTION_LEVELS[
                    currentTrinketArmoryLevelIndex
                  ]
                }
                handleChoiceChange={(currentTrinketArmoryLevel) => {
                  setCurrentTrinketArmoryLevelIndex(
                    TRINKET_ARMORY_COLLECTION_LEVELS.findIndex(
                      (trinketArmoryLevel) =>
                        trinketArmoryLevel === currentTrinketArmoryLevel
                    )
                  );
                }}
              />
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={6}>
          <StatsTable
            title="Trinket Armory Stats"
            color={currentTrinktArmory.color}
            stats={currentTrinktArmory.bonuses.map((bonus) => ({
              name: bonus.name,
              description: bonus.description,
              value: bonus.progression[currentTrinketArmoryLevelIndex],
            }))}
          />
        </Grid>
        {currentTrinktArmory.trinkets.map((trinket, index) => (
          <Grid item xs={12} md={6} key={index}>
            <StatsTable
              title={
                trinket.gear_with_level.find(
                  (trinket) => trinket.level === currentTrinketLevel
                ).name
              }
              color={currentTrinktArmory.color}
              stats={trinket.gear_with_level
                .find((trinket) => trinket.level === currentTrinketLevel)
                .stats.map((stat) => ({
                  name: stat.name,
                  description: stat.description,
                  value: stat.progression[currentQualityIndex],
                }))}
            />
          </Grid>
        ))}
      </Grid>
    </Page>
  );
}

export default TrinketArmory;
