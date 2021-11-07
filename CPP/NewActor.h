// -----------------------------------------------------------
// NewActor.h
// v.1.0
// Updated: 20211107
// -----------------------------------------------------------

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Components/HierarchicalInstancedStaticMeshComponent.h"

// Verify that only a single 'generated.h' file ends this list.
#include "NewActor.generated.h"

UCLASS()
class SANDBOX_CPP_V4271_API ANewActor : public AActor
{
    GENERATED_BODY()

// Verify all properties and functions have a category defined for organization.
public:
    // VARIABLES

    // Bool variable for toggling event from Details panel in Editor.
    UPROPERTY(EditAnywhere, Category = "Actor Setup")
    bool clearStaticMeshes = false;

    // FUNCTIONS

    UFUNCTION(BlueprintCallable, Category = "HansFunctions")
    void ZTestFuncA(UHierarchicalInstancedStaticMeshComponent*& NewHISM, FName Name);

    //UFUNCTION(BlueprintCallable, Category = "HansFunctions")
    //void ZTestFuncC();

public:
    void ZTestFuncC();

public:
    // Sets default values for this actor's properties
    ANewActor();

public:
    // Called when class instance is placed in editor or spawned.
    // It also triggers each time the instance is edited in the editor, which can
    // lead to repeat events.
    virtual void OnConstruction();

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

public:
    // Called after components in array are registered.
    // Can be a potential state for clearing out static mesh components
    // intended to be discarded after conversion.
    virtual void PostRegisterAllComponents() override;

};
