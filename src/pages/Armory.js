import { CardContent } from "@mui/material";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import useLocalStorage from "@rehooks/local-storage";
import React, { useState } from "react";
import { Navigate, useParams } from "react-router-dom";
import NavBar from "../common/NavBar";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import StatsTable from "../common/StatsTable";
import armories from "../data/armory.json";
import GearStatsCard from "./GearStatsCard";

const LEVELS = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];
const ARMORY_COLLECTION_LEVELS = [...Array(236).keys()].map((i) => i + 1);

function Armory() {
  const urlParams = useParams();
  const [currentLevel, setCurrentLevel] = useLocalStorage("armory-level", 40);
  const [currentQualityIndex, setCurrentQualityIndex] = useLocalStorage(
    "armory-quality-index",
    2
  );
  const [currentArmoryLevelIndex, setCurrentArmoryLevelIndex] = useLocalStorage(
    "armory-collection-level",
    165
  );

  if (!urlParams.armoryId) {
    return (
      <Navigate replace to={`/armory/${armories[armories.length - 1].id}`} />
    );
  }

  const armory = armories.find((armory) => armory.id === urlParams.armoryId);
  return (
    <React.Fragment>
      <NavBar
        title="GoTC Armory"
        selectArgsList={[
          {
            name: "gear-set",
            choices: armories.map((armory) => ({
              id: armory.id,
              name: armory.name,
              link: `/armory/${armory.id}`,
            })),
            currentChoiceId: urlParams.armoryId,
          },
        ]}
      />

      <Container maxWidth="lg">
        <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
          <Grid item xs={12} md={6} sx={{ p: 0 }}>
            <Card sx={{ color: "white" }}>
              <CardHeader
                title={armory.name}
                subheader={armory.description}
                style={{ backgroundColor: armory.color }}
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
                      QUALITIES.findIndex(
                        (quality) => quality === currentQuality
                      )
                    );
                  }}
                />
                <SingleChoiceSelect
                  name="armory-level"
                  choices={ARMORY_COLLECTION_LEVELS}
                  currentChoice={
                    ARMORY_COLLECTION_LEVELS[currentArmoryLevelIndex]
                  }
                  handleChoiceChange={(currentArmoryLevel) => {
                    setCurrentArmoryLevelIndex(
                      ARMORY_COLLECTION_LEVELS.findIndex(
                        (armoryLevel) => armoryLevel === currentArmoryLevel
                      )
                    );
                  }}
                />
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} md={6}>
            <StatsTable
              title="Armory Stats"
              color={armory.color}
              stats={["bonus_1", "bonus_2", "bonus_3"].map((bonusName) => ({
                name: armory[bonusName].name,
                description: armory[bonusName].description,
                value: armory[bonusName].progression[currentArmoryLevelIndex],
              }))}
            />
          </Grid>
          {["helmet", "weapon", "chest", "ring", "pants", "boots"].map(
            (slot, index) => (
              <Grid item xs={12} md={6} key={index}>
                <GearStatsCard
                  armory={armory}
                  gear={armory[slot]}
                  currentLevel={currentLevel}
                  currentQualityIndex={currentQualityIndex}
                />
              </Grid>
            )
          )}
        </Grid>
      </Container>
    </React.Fragment>
  );
}

export default Armory;
