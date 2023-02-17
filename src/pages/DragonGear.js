import { CardContent } from "@mui/material";
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
import dragonGearSets from "../data/dragon_gear.json";

const LEVELS = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];

function DragonGear() {
  const urlParams = useParams();
  const [currentLevel, setCurrentLevel] = useLocalStorage("gear-level", 40);
  const [currentQualityIndex, setCurrentQualityIndex] = useLocalStorage(
    "quality-index",
    2
  );

  if (!urlParams.dragonGearSetId) {
    return (
      <Navigate
        replace
        to={`/dragon-gear/${dragonGearSets[dragonGearSets.length - 1].id}`}
      />
    );
  }

  const dragonGearSet = dragonGearSets.find(
    (gearSet) => gearSet.id === urlParams.dragonGearSetId
  );
  return (
    <Page
      title="Dragon Gear Set"
      selectArgsList={[
        {
          name: "dragon-gear-set",
          choices: dragonGearSets.map((gearSet) => ({
            id: gearSet.id,
            name: displayWithRegexFallback(
              gearSet.name,
              new RegExp(/^n:EQ_EVENTS_(\w+)_SET_NAME$/)
            ),
            link: `/dragon-gear/${gearSet.id}`,
          })),
          currentChoiceId: urlParams.dragonGearSetId,
        },
      ]}
    >
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12} md={6} sx={{ p: 0 }}>
          <Card sx={{ color: "white" }}>
            <CardHeader
              title={displayWithRegexFallback(
                dragonGearSet.name,
                new RegExp(/^n:EQ_EVENTS_(\w+)_SET_NAME$/)
              )}
              subheader={displayWithRegexFallback(
                dragonGearSet.description,
                new RegExp(/^n:EQ_EVENTS_(\w+)_SET_DESCRIPTION$/)
              )}
              sx={{ backgroundColor: dragonGearSet.color }}
              subheaderTypographyProps={{ color: "inherit" }}
            />
            <CardContent>
              <SingleChoiceSelect
                name="level"
                choices={LEVELS}
                currentChoice={currentLevel}
                handleChoiceChange={setCurrentLevel}
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
        {["saddle", "chanfron", "peytral"].map((slot, index) => {
          const gear = dragonGearSet[slot];
          return (
            <Grid item xs={12} md={6} key={index}>
              <DataCard
                title={displayWithRegexFallback(
                  gear.gear_with_level.find(
                    (gear) => gear.level === currentLevel
                  ).name,
                  new RegExp(/^n:EQ_EVENTS_(\w+_[0-9]+_\w+)_LORD[0-9]+_NAME$/)
                )}
                color={dragonGearSet.color}
                data={gear.gear_with_level
                  .find((gear) => gear.level === currentLevel)
                  .stats.map((stat) => ({
                    name: stat.name,
                    tooltip: stat.description,
                    value: stat.progression[currentQualityIndex],
                  }))}
              />
            </Grid>
          );
        })}
      </Grid>
    </Page>
  );
}

export default DragonGear;
