import { CardContent } from "@material-ui/core";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import React, { useState } from "react";
import NavBar from "../common/NavBar";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import StatsTable from "../common/StatsTable";
import armories from "../data/armory.json";
import GearStatsCard from "./GearStatsCard";

const LEVELS = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];
const ARMORY_COLLECTION_LEVELS = [...Array(236).keys()].map((i) => i + 1);

const useStyles = makeStyles((theme) => ({
  mainCard: {
    color: "white",
  },
  container: {
    margin: theme.spacing(3, 0, 3, 0),
  },
}));

function Armory() {
  const classes = useStyles();
  const [currentLevel, setCurrentLevel] = useState(40);
  const [currentQualityIndex, setCurrentQualityIndex] = useState(2);
  const [currentArmoryIndex, setCurrentArmoryIndex] = useState(
    armories.length - 1
  );
  const [currentArmoryLevelIndex, setCurrentArmoryLevelIndex] = useState(165);

  const armoryNames = armories.map((armory) => armory.name);
  const armory = armories[currentArmoryIndex];
  const armoryStat1 = armory["bonus_1"];
  console.log(
    `Armory stat 1: ${armoryStat1["name"]} (${armoryStat1["description"]}), value: ${armoryStat1["progression"][currentArmoryLevelIndex]}`
  );

  return (
    <React.Fragment>
      <NavBar
        title="GoTC Armory"
        selectArgsList={[
          {
            name: "gear-set",
            choices: armoryNames,
            currentChoice: armory.name,
            handleChoiceChange: (currentArmoryName) => {
              setCurrentArmoryIndex(
                armoryNames.findIndex(
                  (armoryName) => armoryName === currentArmoryName
                )
              );
            },
          },
        ]}
      />

      <Container maxWidth="lg">
        <Grid container spacing={2} className={classes.container}>
          <Grid item xs={12} md={6}>
            <Card className={classes.mainCard}>
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
            (slot) => (
              <Grid item xs={12} md={6}>
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
