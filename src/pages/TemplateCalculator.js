import Grid from "@mui/material/Grid";
import Page from "../common/Page";
import Box from "@mui/material/Box";
import useLocalStorage from "@rehooks/local-storage";
import SingleChoiceSelect from "../common/SingleChoiceSelect";
import templateData from "../data/template.json";
import TemplateMaterials from "./TemplateMaterials";
import TemplateGoals from "./TemplateGoals";

const LEVELS = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
const QUALITIES = ["Poor", "Common", "Fine", "Exquisite", "Epic", "Legendary"];

function TemplateCalculator() {
  const { materials } = templateData;
  const [currentLevelIndex, setCurrentLevelIndex] = useLocalStorage(
    "template-level-index",
    2
  );
  const [currentQualityIndex, setCurrentQualityIndex] = useLocalStorage(
    "template-quality-index",
    5
  );
  const [numTemplates, setNumTemplates] = useLocalStorage(
    "template-num-templates",
    1
  );
  const [existingTemplates, setExistingTemplates] = useLocalStorage(
    "template-existing-templates",
    []
  );
  const [existingMaterials, setExistingMaterials] = useLocalStorage(
    "template-existing-materials",
    materials.reduce(
      (obj, material) => ({
        ...obj,
        [material.id]: Array(currentQualityIndex + 1).fill(0),
      }),
      {}
    )
  );
  const resetOnLevelChange = (newLevelIndex) => {
    setNumTemplates(1);
    setExistingTemplates(Array(newLevelIndex).fill(0));
  };
  const resetOnQualityChange = (newQualityIndex) => {
    setExistingMaterials(
      materials.reduce(
        (obj, material) => ({
          ...obj,
          [material.id]: Array(newQualityIndex + 1).fill(0),
        }),
        {}
      )
    );
  };

  return (
    <Page title="Template Calculator">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12} md={6} sx={{ p: 0 }}>
          <Box sx={{ py: 1 }}>
            <SingleChoiceSelect
              name="level"
              choices={LEVELS}
              currentChoice={LEVELS[currentLevelIndex]}
              handleChoiceChange={(currentLevel) => {
                const newLevelIndex = LEVELS.findIndex(
                  (level) => level === currentLevel
                );
                setCurrentLevelIndex(newLevelIndex);
                resetOnLevelChange(newLevelIndex);
              }}
            />
            <SingleChoiceSelect
              name="quality"
              choices={QUALITIES}
              currentChoice={QUALITIES[currentQualityIndex]}
              handleChoiceChange={(currentQuality) => {
                const newQualityIndex = QUALITIES.findIndex(
                  (quality) => quality === currentQuality
                );
                setCurrentQualityIndex(newQualityIndex);
                resetOnQualityChange(newQualityIndex);
              }}
            />
          </Box>
          <Box
            sx={{
              py: 1,
            }}
          >
            <TemplateMaterials
              materials={materials}
              qualities={QUALITIES.slice(0, currentQualityIndex + 1)}
              existingMaterials={existingMaterials}
              setExistingMaterials={setExistingMaterials}
            />
          </Box>
          <Box
            sx={{
              py: 1,
            }}
          >
            <TemplateGoals
              levels={LEVELS.slice(0, currentLevelIndex + 1)}
              existingTemplates={existingTemplates}
              setExistingTemplates={setExistingTemplates}
              numTemplates={numTemplates}
              setNumTemplates={setNumTemplates}
            />
          </Box>
        </Grid>
      </Grid>
    </Page>
  );
}

export default TemplateCalculator;
