import Grid from "@mui/material/Grid";
import DataTable from "../common/DataTable";
import Page from "../common/Page";
import recipes from "../data/recipe.json";

function getIngredientValue(ingredients, index) {
  if (index >= ingredients.length) return "";
  const ingredient = ingredients[index];
  return `(${ingredient.quantity}x) ${ingredient.name}`;
}

function getIngredientTooltip(ingredients, index) {
  if (index >= ingredients.length) return "";
  return ingredients[index].description;
}

function Recipe() {
  return (
    <Page title="Recipes">
      <Grid container spacing={2} sx={{ px: 0, py: 2 }}>
        <Grid item xs={12}>
          <DataTable
            title="Recipes"
            storageKey="recipe-table-state"
            data={recipes}
            searchKeysAccessor={(recipe) =>
              [
                recipe.name,
                recipe.description,
                recipe.category,
                recipe.event_name,
              ] + recipe.ingredients.map((ingredient) => ingredient.name)
            }
            columnConfigs={[
              {
                name: "Name",
                valueType: "text",
                valueAccessor: (recipe) =>
                  recipe.limit
                    ? `${recipe.name} (limit ${recipe.limit})`
                    : recipe.name,
                tooltipAccessor: (recipe) => recipe.description,
                options: { filter: false },
              },
              {
                name: "Category",
                valueType: "text",
                valueAccessor: (recipe) => recipe.category,
                options: { filter: true },
              },
              {
                name: "Event",
                valueType: "text",
                valueAccessor: (recipe) => recipe.event_name,
                options: { filter: true },
              },
              {
                name: "Event Points",
                valueType: "number",
                valueAccessor: (recipe) => recipe.event_points,
                options: { filter: false },
              },
              {
                name: "Ingredient 1",
                valueType: "text",
                valueAccessor: (recipe) =>
                  getIngredientValue(recipe.ingredients, 0),
                tooltipAccessor: (recipe) =>
                  getIngredientTooltip(recipe.ingredients, 0),
                options: { filter: false },
              },
              {
                name: "Ingredient 1",
                valueType: "text",
                valueAccessor: (recipe) =>
                  getIngredientValue(recipe.ingredients, 1),
                tooltipAccessor: (recipe) =>
                  getIngredientTooltip(recipe.ingredients, 1),
                options: { filter: false },
              },
            ]}
            options={{
              filter: true,
              rowsPerPage: 20,
              rowsPerPageOptions: [10, 15, 20],
            }}
          />
        </Grid>
      </Grid>
    </Page>
  );
}

export default Recipe;
