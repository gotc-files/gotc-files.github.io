import CardContent from "@mui/material/CardContent";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import Grid from "@mui/material/Grid";
import useLocalStorage from "@rehooks/local-storage";
import React from "react";
import { Navigate, useParams } from "react-router-dom";
import DataCard from "../common/DataCard";
import Page from "../common/Page";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import { displayWithRegexFallback } from "../common/util";
import trinketArmories from "../data/trinket_armory.json";

const LEVELS = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];

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
  const [currentTrinketArmoryLevel, setCurrentTrinketArmoryLevel] =
    useLocalStorage("trinket-armory-collection-level", 105);

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
            name: displayWithRegexFallback(
              trinketArmory.name,
              new RegExp(/n:EQ_TRINKET_(\w+)_1_SET_NAME/)
            ),
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
              title={displayWithRegexFallback(
                currentTrinktArmory.name,
                new RegExp(/n:EQ_TRINKET_(\w+)_1_SET_NAME/)
              )}
              style={{ backgroundColor: currentTrinktArmory.color }}
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
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={6}>
          <DataCard
            title={`Trinket Armory Stats (${currentTrinketArmoryLevel})`}
            color={currentTrinktArmory.color}
            slider={{
              min: 1,
              max: 150,
              value: currentTrinketArmoryLevel,
              setValue: setCurrentTrinketArmoryLevel,
            }}
            data={currentTrinktArmory.bonuses.map((bonus) => ({
              name: bonus.name,
              tooltip: bonus.description,
              value: bonus.progression[currentTrinketArmoryLevel - 1],
            }))}
          />
        </Grid>
        {currentTrinktArmory.trinkets.map((trinket, index) => (
          <Grid item xs={12} md={6} key={index}>
            <DataCard
              title={displayWithRegexFallback(
                trinket.gear_with_level.find(
                  (trinket) => trinket.level === currentTrinketLevel
                ).name,
                new RegExp(
                  /n:EQ_EVENTS_(TRINKET_\w+_[0-9]+)_TRINKET_LORD40_NAME/
                )
              )}
              color={currentTrinktArmory.color}
              data={trinket.gear_with_level
                .find((trinket) => trinket.level === currentTrinketLevel)
                .stats.map((stat) => ({
                  name: stat.name,
                  tooltip: stat.description,
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
