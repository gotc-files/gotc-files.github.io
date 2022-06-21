import GLPK from "glpk.js";

class TemplateCalculator {
  constructor() {
    this.glpkPromise = GLPK();
  }

  async calculate(existingMaterials, goals, recipes) {
    const glpk = await this.glpkPromise;
    const problem = {
      name: "Crafting Template Optimization",
      objective: {
        direction: glpk.GLP_MAX,
        name: "Max Left Over",
        vars: [{ name: "left-over", coef: 1 }],
      },
      subjectTo: [],
      generals: ["left-over"],
      options: {
        msglev: glpk.GLP_MSG_ERR,
        presol: true,
        mipgap: 1,
        tmlim: 10,
      },
    };
    const goalConstraints = {};
    for (const [level, num] of Object.entries(goals)) {
      goalConstraints[level] = {
        name: `g${level}`,
        vars: [],
        bnds: { type: glpk.GLP_FX, ub: num, lb: num },
      };
    }
    const materialConstraints = {};
    for (const [materialId, num] of Object.entries(existingMaterials)) {
      materialConstraints[materialId] = {
        name: materialId,
        vars: [
          {
            name: "left-over",
            coef: 1,
          },
        ],
        bnds: {
          type: glpk.GLP_UP,
          ub: num,
        },
      };
    }
    recipes.forEach((recipe) => {
      if (!(recipe.level in goalConstraints)) {
        return;
      }
      problem.generals.push(recipe.id);
      goalConstraints[recipe.level].vars.push({
        name: recipe.id,
        coef: 1,
      });
      recipe.ingredients.forEach(({ id: materialId, quantity }) => {
        materialConstraints[materialId].vars.push({
          name: recipe.id,
          coef: quantity,
        });
      });
    });
    problem.subjectTo.push(...Object.values(goalConstraints));
    problem.subjectTo.push(...Object.values(materialConstraints));
    const { result } = glpk.solve(problem);

    if (result.status !== glpk.GLP_OPT && result.status !== glpk.GLP_FEAS) {
      console.log(
        `Cannot optimize crafting templates, status: ${result.status}`
      );
      return null;
    }
    return Object.entries(result.vars)
      .filter((entry) => entry[0] !== "left-over")
      .map(([recipeId, quantity]) => ({
        recipe: recipeId,
        quantity,
      }));
  }
}

export default TemplateCalculator;
