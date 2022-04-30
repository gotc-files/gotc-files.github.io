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
import armories from "../data/armory.json";

const LEVELS = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];

function Armory() {
  const urlParams = useParams();
  const [currentLevel, setCurrentLevel] = useLocalStorage("gear-level", 40);
  const [currentQualityIndex, setCurrentQualityIndex] = useLocalStorage(
    "quality-index",
    2
  );
  const [currentArmoryLevel, setCurrentArmoryLevel] = useLocalStorage(
    "armory-collection-level",
    166
  );

  if (!urlParams.armoryId) {
    return (
      <Navigate replace to={`/armory/${armories[armories.length - 1].id}`} />
    );
  }

  const armory = armories.find((armory) => armory.id === urlParams.armoryId);
  return (
    <Page
      title="Armory"
      selectArgsList={[
        {
          name: "gear-set",
          choices: armories.map((armory) => ({
            id: armory.id,
            name: displayWithRegexFallback(
              armory.name,
              new RegExp(/^n:EQ_EVENTS_(\w+)_SET_NAME$/)
            ),
            link: `/armory/${armory.id}`,
          })),
          currentChoiceId: urlParams.armoryId,
        },
      ]}
    >
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12} md={6} sx={{ p: 0 }}>
          <Card sx={{ color: "white" }}>
            <CardHeader
              title={displayWithRegexFallback(
                armory.name,
                new RegExp(/^n:EQ_EVENTS_(\w+)_SET_NAME$/)
              )}
              subheader={displayWithRegexFallback(
                armory.name,
                new RegExp(/^n:EQ_EVENTS_(\w+)_SET_NAME$/)
              )}
              sx={{ backgroundColor: armory.color }}
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
        <Grid item xs={12} md={6}>
          <DataCard
            title={`Armory Stats (${currentArmoryLevel})`}
            color={armory.color}
            slider={{
              min: 1,
              max: 236,
              value: currentArmoryLevel,
              setValue: setCurrentArmoryLevel,
            }}
            data={["bonus_1", "bonus_2", "bonus_3"].map((bonusName) => ({
              name: armory[bonusName].name,
              tooltip: armory[bonusName].description,
              value: armory[bonusName].progression[currentArmoryLevel - 1],
            }))}
          />
        </Grid>
        {["helmet", "weapon", "chest", "ring", "pants", "boots"].map(
          (slot, index) => {
            const gear = armory[slot];
            return (
              <Grid item xs={12} md={6} key={index}>
                <DataCard
                  title={displayWithRegexFallback(
                    gear.gear_with_level.find(
                      (gear) => gear.level === currentLevel
                    ).name,
                    new RegExp(/^n:EQ_EVENTS_(\w+_[0-9]+_\w+)_LORD[0-9]+_NAME$/)
                  )}
                  color={armory.color}
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
          }
        )}
      </Grid>
    </Page>
  );
}

export default Armory;
