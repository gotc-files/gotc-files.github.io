import TemplateCalculator from "./TemplateCalculator";
import templateData from "../data/template.json";

test("calculates a single recipe", async () => {
  expect(
    await new TemplateCalculator().calculate(
      {
        m1: 10,
        m2: 10,
      },
      { 1: 1 },
      [
        {
          id: "r1",
          ingredients: [
            {
              id: "m1",
              quantity: 10,
            },
            {
              id: "m2",
              quantity: 10,
            },
          ],
          level: 1,
        },
      ]
    )
  ).toEqual([{ recipe: "r1", quantity: 1 }]);
});

test("calculates a real scenario with all the recipes", async () => {
  const { materials, recipes } = templateData;

  const recipesToCraft = await new TemplateCalculator().calculate(
    materials.reduce((obj, material) => ({ ...obj, [material.id]: 3222 }), {}),
    { 1: 351, 5: 351, 10: 351 },
    recipes
  );
  const recipeFromId = Object.fromEntries(
    recipes.map((recipe) => [recipe.id, recipe])
  );
  expect(
    materials
      .map(({ id: currentMaterialId }) =>
        recipesToCraft.reduce(
          (partialSum, { recipe, quantity: recipeQuantity }) =>
            partialSum +
            recipeQuantity *
              recipeFromId[recipe].ingredients.reduce(
                (
                  partialNumMaterials,
                  { id: materialId, quantity: materialQuantity }
                ) =>
                  partialNumMaterials +
                  (materialId === currentMaterialId ? materialQuantity : 0),
                0
              ),
          0
        )
      )
      .reduce((partialSum, numMaterials) => partialSum + numMaterials, 0)
  ).toEqual(38610);
});
